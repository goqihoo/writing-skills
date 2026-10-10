import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EVALUATOR = REPO_ROOT / "scripts" / "evaluate_document.py"


class EvaluateDocumentTest(unittest.TestCase):
    def test_accepts_prose_changes_and_rejects_structural_or_logical_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source = temp_path / "source.md"
            good_candidate = temp_path / "good.md"
            bad_candidate = temp_path / "bad.md"
            contract = temp_path / "contract.json"

            source.write_text(
                """# RWA 的本质

## 领域定义

资产、持有人权利和代币状态是不同对象。

## 核心转换

代币状态必须持续对应链下权利。

详见 [对象映射](<Asset and Rights Mapping.md>)。
""",
                encoding="utf-8",
            )
            good_candidate.write_text(
                """# RWA 的本质

## 领域定义

现实资产不会因为代币发行而进入区块链。资产、持有人权利和代币状态仍是三个不同对象。

## 核心转换

产品必须让代币状态持续对应链下权利，即使现实事实已经发生变化。

进一步的对象关系见 [对象映射](<Asset and Rights Mapping.md>)。
""",
                encoding="utf-8",
            )
            bad_candidate.write_text(
                """# RWA 的本质

## Alice 买到了什么？

Alice 在钱包里看到一枚代币。

## 如何判断一个 RWA 产品？

先查看它使用哪一种代币标准。
""",
                encoding="utf-8",
            )
            contract.write_text(
                json.dumps(
                    {
                        "preserve_heading_sequence": True,
                        "preserve_relative_links": True,
                        "required_patterns": [
                            {
                                "name": "maintained_correspondence",
                                "pattern": "代币状态.*链下权利",
                            }
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            good_result = self.run_evaluator(source, good_candidate, contract)
            self.assertEqual(0, good_result.returncode, good_result.stderr)
            self.assertIn("PASS: document contract satisfied", good_result.stdout)

            bad_result = self.run_evaluator(source, bad_candidate, contract)
            self.assertEqual(1, bad_result.returncode, bad_result.stderr)
            self.assertIn("heading sequence changed", bad_result.stdout)
            self.assertIn("relative Markdown links changed", bad_result.stdout)
            self.assertIn(
                "required pattern missing: maintained_correspondence",
                bad_result.stdout,
            )

    def test_limits_type_labels_used_as_headings_for_new_knowledge(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source = temp_path / "source.md"
            good_candidate = temp_path / "good.md"
            bad_candidate = temp_path / "bad.md"
            contract = temp_path / "contract.json"

            source.write_text("# Topic\n", encoding="utf-8")
            good_candidate.write_text(
                """# The Essence of RWA

## The Asset Does Not Move On-Chain

## Correspondence Is the Product

## Why Correspondence Breaks
""",
                encoding="utf-8",
            )
            bad_candidate.write_text(
                """# The Essence of RWA

## Definition and Scope

## Core Objects

## Core Transformation

## Necessary Conditions
""",
                encoding="utf-8",
            )
            contract.write_text(
                json.dumps(
                    {
                        "heading_match_limit": {
                            "headings": [
                                "Definition and Scope",
                                "Core Objects",
                                "Core Transformation",
                                "Necessary Conditions",
                            ],
                            "levels": [2],
                            "max_matches": 2,
                        }
                    }
                ),
                encoding="utf-8",
            )

            good_result = self.run_evaluator(source, good_candidate, contract)
            self.assertEqual(0, good_result.returncode, good_result.stderr)

            bad_result = self.run_evaluator(source, bad_candidate, contract)
            self.assertEqual(1, bad_result.returncode, bad_result.stderr)
            self.assertIn(
                "heading match limit exceeded: 4 matches, maximum 2",
                bad_result.stdout,
            )

    def test_preserves_architecture_template_order_with_allowed_omissions(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            template = temp_path / "template.md"
            good_candidate = temp_path / "good.md"
            bad_candidate = temp_path / "bad.md"
            missing_h2_candidate = temp_path / "missing-h2.md"
            contract = temp_path / "contract.json"

            template.write_text(
                """# <System> Architecture

## Document status

## Context

## Architecture

### System context and boundaries

### Responsibilities and authoritative state

## Validation
""",
                encoding="utf-8",
            )
            good_candidate.write_text(
                """# Payment Architecture

## Document status

## Context

## Architecture

### System context and boundaries

## Validation
""",
                encoding="utf-8",
            )
            bad_candidate.write_text(
                """# Payment Architecture

## Architecture

### Components

## Context

## Validation
""",
                encoding="utf-8",
            )
            missing_h2_candidate.write_text(
                """# Payment Architecture

## Document status

## Architecture

### System context and boundaries

## Validation
""",
                encoding="utf-8",
            )
            contract.write_text(
                json.dumps(
                    {
                        "template_heading_sequence": {
                            "ignore_title": True,
                            "allow_omissions": True,
                            "required_levels": [2],
                        }
                    }
                ),
                encoding="utf-8",
            )

            good_result = self.run_evaluator(template, good_candidate, contract)
            self.assertEqual(0, good_result.returncode, good_result.stderr)

            bad_result = self.run_evaluator(template, bad_candidate, contract)
            self.assertEqual(1, bad_result.returncode, bad_result.stderr)
            self.assertIn("template heading sequence changed", bad_result.stdout)

            missing_h2_result = self.run_evaluator(
                template, missing_h2_candidate, contract
            )
            self.assertEqual(1, missing_h2_result.returncode, missing_h2_result.stderr)
            self.assertIn(
                "required template headings missing: ['2:Context']",
                missing_h2_result.stdout,
            )

    def test_requires_complete_delivery_template_when_omissions_are_disabled(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            template = temp_path / "template.md"
            good_candidate = temp_path / "good.md"
            bad_candidate = temp_path / "bad.md"
            contract = temp_path / "contract.json"

            template.write_text(
                """# <System> Architecture

## Context

## Architecture

## Validation
""",
                encoding="utf-8",
            )
            good_candidate.write_text(
                """# Payment Architecture

## Context

## Architecture

## Validation
""",
                encoding="utf-8",
            )
            bad_candidate.write_text(
                """# Payment Architecture

## Context

## Architecture
""",
                encoding="utf-8",
            )
            contract.write_text(
                json.dumps(
                    {
                        "template_heading_sequence": {
                            "ignore_title": True,
                            "allow_omissions": False,
                        }
                    }
                ),
                encoding="utf-8",
            )

            good_result = self.run_evaluator(template, good_candidate, contract)
            self.assertEqual(0, good_result.returncode, good_result.stderr)

            bad_result = self.run_evaluator(template, bad_candidate, contract)
            self.assertEqual(1, bad_result.returncode, bad_result.stderr)
            self.assertIn("template heading sequence changed", bad_result.stdout)

    def run_evaluator(
        self, source: Path, candidate: Path, contract: Path
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(EVALUATOR),
                "--source",
                str(source),
                "--candidate",
                str(candidate),
                "--contract",
                str(contract),
            ],
            capture_output=True,
            text=True,
            check=False,
        )


if __name__ == "__main__":
    unittest.main()
