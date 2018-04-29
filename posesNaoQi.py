class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        # put initialization code here
        pass

    def onUnload(self):
        # put clean-up code here
        pass

    def pose1(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0.15])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-2])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-1.3894])

        names.append("LHand")
        times.append([1.08])
        keys.append([1])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.299871])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([2])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.3894])

        names.append("RHand")
        times.append([1.08])
        keys.append([1])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([1.3994])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0.299871])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([1])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose2(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0.15])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0.2])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-1.3894])

        names.append("LHand")
        times.append([1.08])
        keys.append([0.30])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.299871])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([1.44])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.3894])

        names.append("RHand")
        times.append([1.08])
        keys.append([1])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([0.965])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0.39862])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose3(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-1.3894])

        names.append("LHand")
        times.append([1.08])
        keys.append([0])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.367])

        names.append("RHand")
        times.append([1.08])
        keys.append([0])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([1.3994])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose4(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-0.56])

        names.append("LHand")
        times.append([1.08])
        keys.append([0])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([1.876])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([-0.76])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.367])

        names.append("RHand")
        times.append([1.08])
        keys.append([0])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose5(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-1.367])

        names.append("LHand")
        times.append([1.08])
        keys.append([0])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.367])

        names.append("RHand")
        times.append([1.08])
        keys.append([0])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose6(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.23])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-1.765])

        names.append("LHand")
        times.append([1.08])
        keys.append([1])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([1.367])

        names.append("RHand")
        times.append([1.08])
        keys.append([0])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([1])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose7(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-0.65])

        names.append("LHand")
        times.append([1.08])
        keys.append([1])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([0.65])

        names.append("RHand")
        times.append([1.08])
        keys.append([1])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)


    def pose8(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0.65])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-0.65])

        names.append("LHand")
        times.append([1.08])
        keys.append([1])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([1.9])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([0.65])

        names.append("RHand")
        times.append([1.08])
        keys.append([1])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([1.9])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose9(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.08])
        keys.append([0])

        names.append("HeadYaw")
        times.append([1.08])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([1.08])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([1.08])
        keys.append([-0])

        names.append("LHand")
        times.append([1.08])
        keys.append([1])

        names.append("LHipPitch")
        times.append([1.08])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("LKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([1.08])
        keys.append([0.5])

        names.append("LShoulderRoll")
        times.append([1.08])
        keys.append([0.2])

        names.append("LWristYaw")
        times.append([1.08])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([1.08])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([1.08])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([1.08])
        keys.append([0])

        names.append("RHand")
        times.append([1.08])
        keys.append([1])

        names.append("RHipPitch")
        times.append([1.08])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([1.08])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([1.08])
        keys.append([0])

        names.append("RKneePitch")
        times.append([1.08])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([1.08])
        keys.append([0.5])

        names.append("RShoulderRoll")
        times.append([1.08])
        keys.append([-0.2])

        names.append("RWristYaw")
        times.append([1.08])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)



    def onInput_onStart(self):
        # Choregraphe simplified export in Python.
        from naoqi import ALProxy

        poses = 1
        #self.pose1()
        #self.pose2()
        #self.pose3()
        #self.pose4()
        #self.pose5()
        #self.pose6()
        #self.pose7()
        #self.pose8()
        #self.pose9()

        # activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload()  # it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  # activate the output of the box
