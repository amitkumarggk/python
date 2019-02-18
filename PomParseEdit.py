#
# parsing maven pom.xml
# updating version with ci_owner_repo_SNAPSHOT
#
from xml.etree import ElementTree
import giturlparse
class PomParseEdit:
   def pom_parse_edit(self):
       url = giturlparse.parse('ssh://git@gitlab.com:3333/org/repo.git')
       print "owner::"+url.owner
       print "repo:::"+url.repo
       latest_version='_'.join(['ci',url.owner,url.repo,'SNAPSHOT'])
       POM_FILE="pom.xml"
       namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}
       tree = ElementTree.parse(POM_FILE)
       root = tree.getroot()
       version = root.find("xmlns:version", namespaces=namespaces)
       print  "old version"+version.text
       root.find("xmlns:version", namespaces=namespaces).text=latest_version
       tree.write("pom.xml")
       version = root.find("xmlns:version", namespaces=namespaces)
       return version.text

if __name__ == '__main__':
    pomParseEdit = PomParseEdit()
    print('version updated with:::', pomParseEdit.pom_parse_edit())
