#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Priority_queue:
    class _Node:
        def __init__(self, data, priority):
            self._data=data
            self._priority= priority
            
    def __init__(self):
        self._queue = list()
        self._hashmap = {}
        
    def insert(self, data, priority):
        new_node = self._Node(data,priority)
        self._queue.append(new_node._data)
        key= new_node._priority
        if key not in self._hashmap.keys():
            self._hashmap[key] = [new_node._data]
        else:
            self._hashmap[key].append(new_node._data)
          
    def _get_priority_list(self):
        _priority_list = list(self._hashmap.keys())
        _priority_list = sorted(_priority_list)
        return _priority_list
        
    def remove_item(self):
        try:
            x = self._get_priority_list()   
            _max_priority = max(x)
            _max_priority_queue = self._hashmap[_max_priority]
            _removed_ele = _max_priority_queue.pop(0)
            self._queue.remove(_removed_ele)
            if len(_max_priority_queue)==0:
                del self._hashmap[_max_priority]
                #max_priority_queue.remove(max_priority)
            return 'High Priority ele removed is {}'.format(_removed_ele) 
        except:
            raise Exception('Queue is empty')
    
    def get_size(self):
        return len(self._queue)
    
    def print_queue(self):
        max_counter = len(self._queue)
        min_counter = 0
        while min_counter<max_counter:
            print(self._queue[min_counter])
            min_counter+=1

