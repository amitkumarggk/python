
import unittest
import PomParseEdit as PomParseEditClass

class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    pomParseEditTest = PomParseEditClass.PomParseEdit()
    def test_0_pom_parse_edit(self):
        print("Start pom_parse_edit test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        name = "ci_org_repo_SNAPSHOT"
        self.assertEqual(name, self.pomParseEditTest.pom_parse_edit())
        print(self.pomParseEditTest.pom_parse_edit())
        print("\nFinish pom_parse_edit test\n")

if __name__ == '__main__':
    unittest.main()
