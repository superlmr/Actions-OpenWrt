from pathlib import Path
import unittest

import yaml


class ReleasePermissionsTest(unittest.TestCase):
    def test_build_job_can_publish_release(self):
        workflow_path = Path(__file__).resolve().parents[1] / ".github/workflows/build-openwrt.yml"
        workflow = yaml.load(workflow_path.read_text(), Loader=yaml.BaseLoader)
        build = workflow["jobs"]["build"]

        self.assertEqual(build["permissions"], {"contents": "write"})
        self.assertTrue(
            any(step.get("uses", "").startswith("softprops/action-gh-release@") for step in build["steps"])
        )


if __name__ == "__main__":
    unittest.main()
