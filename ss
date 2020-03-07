        if len(topic) != 0:
            # check topic
            for row in topic:
                # topic already has
                if command[2] in topic[row]:
                    print('have')
                    check = 1
            
            # check topic (do not have)
            if check == 0:
              print('dont have')
              print(countTopic) 
              data = ("{topic: %s, msg: %s}" %(command[1],command[2]))
              topic[countTopic].append(data)
              countTopic += 1
              
        else:
            print('dont have jingjing')
            data = ("{topic: %s, msg: %s}" %(command[1],command[2]))
            topic[countTopic].append(data)
            countTopic += 1 



            def checkTopic(topic_in):
  topicFound = 0
  for row in topicDict:
    # topic already has
    if topic_in == topicDict[row]:
      topicFound = 1
      return row
  if topicFound == 0:
    return 0

def searchTopic(topic_in):
    for item in topicDict:
        print("item %s" %(topicDict[item]['topic']))
        #if topicDict[item]['topic'] == topic_in:
        #   return item
        #else: return 0
    return 0