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
