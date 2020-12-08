import sofaros
  
def recv(data, datafield):
        datafield.value = data.tolist()
        
def createScene(rootNode):
        sofaros.init("SofaNode")

        a.createObject("MechanicalObject", name="receiver", position=[0.0,0.0,0.0])
        a.receiver.showObject=True
        a.receiver.showObjectScale=10.0
        
        sofaros.RosReceiver(rootNode, 
                            "/aruco/tracker/position", 
                            a.receiver.findData("position"), 
                            sofaros.numpy_msg(sofaros.Floats), recv)
        
