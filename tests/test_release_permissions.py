from pathlib import Path
import unittest

import yaml


class ReleasePermissionsTest(unittest.TestCase):
    def load_build_job(self):
        workflow_path = Path(__file__).resolve().parents[1] / ".github/workflows/build-openwrt.yml"
        workflow = yaml.load(workflow_path.read_text(), Loader=yaml.BaseLoader)
        return workflow["jobs"]["build"]

    def test_build_job_can_publish_release(self):
        build = self.load_build_job()

        self.assertEqual(build["permissions"], {"contents": "write"})
        self.assertTrue(
            any(step.get("uses", "").startswith("softprops/action-gh-release@") for step in build["steps"])
        )

    def test_build_job_does_not_delete_workflow_history(self):
        build = self.load_build_job()
        self.assertFalse(
            any(step.get("uses", "").startswith("GitRML/delete-workflow-runs@") for step in build["steps"])
        )


if __name__ == "__main__":
    unittest.main()
