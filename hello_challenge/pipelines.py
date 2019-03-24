# -*- coding: utf-8 -*-
import json
from treelib import Tree, Node

tree = Tree()

class HelloChallengePipeline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.close()
        tree.show()
        tree.save2file('tree.txt')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        
        self.file.write(line)

        option = dict(item)['option']
        value = dict(item)['value']
        
        try:
            if option:
                tree.create_node(value, value.lower(), parent=option.lower())
            else:
                tree.create_node(value, value.lower())
        except:
            pass

