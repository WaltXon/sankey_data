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


def test():
    data = SankeyD()
    data.addNode(0, 'node0')
    data.addNode(1, 'node1')
    data.addNode(2, 'node2')
    data.addNode(3, 'node3')
    data.addNode(4, 'node4')
    data.addNode(5, 'node5')

    data.addLink('node0', 'node1', 1.0)
    data.addLink('node1', 'node2', 1.0)
    data.addLink('node2', 'node3', 0.5)
    data.addLink('node2', 'node4', 0.5)
    data.addLink('node4', 'node5', 0.5)

    data.toString()
    print ("JSON: {0}".format(data.toJSON()))

test()
