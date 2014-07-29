# {
# "nodes":[
# {"node":0,"name":"node0"},
# {"node":1,"name":"node1"},
# {"node":2,"name":"node2"},
# {"node":3,"name":"node3"},
# {"node":4,"name":"node4"}
# ],
# "links":[
# {"source":0,"target":2,"value":2},
# {"source":1,"target":2,"value":2},
# {"source":1,"target":3,"value":2},
# {"source":0,"target":4,"value":2},
# {"source":2,"target":3,"value":2},
# {"source":2,"target":4,"value":2},
# {"source":3,"target":4,"value":4}
# ]}


import json

class SankeyD:
    def __init__(self):
        self.nodes = []
        self.nodeRef = {}
        self.links = []

    def addNode(self, id, name):
        self.nodes.append({'node': id, 'name': name})
        self.nodeRef.setdefault(name, id)

    def addLink(self, source, target, value):
        self.links.append({'source': self.nodeRef[source], 'target': self.nodeRef[target], 'value':value})

    def toJSON(self, indent=False):

        self.data = {"nodes": self.nodes, 'links': self.links}
        if indent == True:
            data_string = json.dumps(self.data, indent=2)
        else:
            data_string = json.dumps(self.data)
        return data_string

    def toString(self):
        print "Nodes = {0}".format(self.nodes)
        print "Links = {0}".format(self.links)

    def save(self, filename):
        self.data = {"nodes": self.nodes, 'links': self.links}
        with open(filename, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)



def test():
    data = SankeyD()
    data.addNode(0, 'State of Texas')
    data.addNode(1, 'Davy Crockett')
    data.addNode(2, 'Jim Bob Moore')
    data.addNode(3, 'Linda Heartattack')
    data.addNode(4, 'Alice Answers')
    data.addNode(5, 'Nathan Nerdowell')

    data.addLink('State of Texas', 'Davy Crockett', 1.0)
    data.addLink('Davy Crockett', 'Jim Bob Moore', 1.0)
    data.addLink('Jim Bob Moore','Linda Heartattack', 0.5)
    data.addLink('Jim Bob Moore', 'Alice Answers', 0.5)
    data.addLink('Alice Answers', 'Nathan Nerdowell', 0.5)

    data.toString()
    print ("JSON: {0}".format(data.toJSON()))

    data.save('saveddata.json')

test()
