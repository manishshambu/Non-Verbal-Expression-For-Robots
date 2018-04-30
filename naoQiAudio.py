from naoqi import ALProxy

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):

        try:
            aup = ALProxy("ALAudioPlayer")
        except Exception,e:
            print "Could not create proxy to ALAudioPlayer"
            print "Error was: ",e
            sys.exit(1)

        #Launchs the playing of a file
        aup.playFile("/Users/manishshambu/Downloads/audio.wav")

        time.sleep(1.0)

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box