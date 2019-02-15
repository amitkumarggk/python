#
# parsing maven pom.xml
# updating version with ci_owner_repo_SNAPSHOT
#
from xml.etree import ElementTree
import giturlparse
url = giturlparse.parse('ssh://git@gitlab.com:3333/org/repo.git')
print url.owner
print url.repo
latest_version='_'.join(str(ci_),url.owner,url.repo,str(SNAPSHOT))

POM_FILE="pom.xml"

print  latest_version.text

namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}

tree = ElementTree.parse(POM_FILE)
root = tree.getroot()
version = root.find("xmlns:version", namespaces=namespaces)
print  version.text
root.find("xmlns:version", namespaces=namespaces).text=latest_version
tree.write("pom.xml")
version = root.find("xmlns:version", namespaces=namespaces)
print version.text
