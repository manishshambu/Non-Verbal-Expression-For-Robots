class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        # put initialization code here
        pass

    def onUnload(self):
        # put clean-up code here
        pass

    def pose0(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0.15])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-2])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-1.3894])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.299871])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([2])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.3894])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([1.3994])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0.299871])

        names.append("RWristYaw")
        times.append([t])
        keys.append([1])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose1(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0.15])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0.2])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-1.98])

        names.append("LHand")
        times.append([t])
        keys.append([0.30])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.299871])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([1.00956])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.98])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.965])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0.39862])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose2(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-1.3894])

        names.append("LHand")
        times.append([t])
        keys.append([0])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([1.3994])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.367])

        names.append("RHand")
        times.append([t])
        keys.append([0])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([1.3994])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose3(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-0.56])

        names.append("LHand")
        times.append([t])
        keys.append([0])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([1.876])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([-0.76])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.367])

        names.append("RHand")
        times.append([t])
        keys.append([0])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose4(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.00956])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-1.367])

        names.append("LHand")
        times.append([t])
        keys.append([0])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.367])

        names.append("RHand")
        times.append([t])
        keys.append([0])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose5(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.23])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-1.765])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([0.87])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([1.367])

        names.append("RHand")
        times.append([t])
        keys.append([0])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([1])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose6(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-0.65])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([0.65])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.35])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0.35])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose7(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0.65])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-0.65])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([1.9])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.35])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([0.65])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([1.9])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0.35])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose8(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1.98])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-0])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([0.5])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([0.2])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([1.98])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([0])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.5])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-0.2])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def pose9(self, t):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([t])
        keys.append([0])

        names.append("HeadYaw")
        times.append([t])
        keys.append([0])

        names.append("LAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("LAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("LElbowRoll")
        times.append([t])
        keys.append([-1])

        names.append("LElbowYaw")
        times.append([t])
        keys.append([-0.5])

        names.append("LHand")
        times.append([t])
        keys.append([1])

        names.append("LHipPitch")
        times.append([t])
        keys.append([-0.45])

        names.append("LHipRoll")
        times.append([t])
        keys.append([0])

        names.append("LHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("LKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("LShoulderPitch")
        times.append([t])
        keys.append([0.5])

        names.append("LShoulderRoll")
        times.append([t])
        keys.append([1.0])

        names.append("LWristYaw")
        times.append([t])
        keys.append([0.9876])

        names.append("RAnklePitch")
        times.append([t])
        keys.append([-0.35])

        names.append("RAnkleRoll")
        times.append([t])
        keys.append([0])

        names.append("RElbowRoll")
        times.append([t])
        keys.append([1])

        names.append("RElbowYaw")
        times.append([t])
        keys.append([0.5])

        names.append("RHand")
        times.append([t])
        keys.append([1])

        names.append("RHipPitch")
        times.append([t])
        keys.append([-0.49])

        names.append("RHipRoll")
        times.append([t])
        keys.append([0])

        names.append("RHipYawPitch")
        times.append([t])
        keys.append([0])

        names.append("RKneePitch")
        times.append([t])
        keys.append([0.7])

        names.append("RShoulderPitch")
        times.append([t])
        keys.append([0.5])

        names.append("RShoulderRoll")
        times.append([t])
        keys.append([-1.0])

        names.append("RWristYaw")
        times.append([t])
        keys.append([0])

        motion = ALProxy("ALMotion")
        motion.angleInterpolation(names, keys, times, True)

    def onInput_onStart(self):
        # Choregraphe simplified export in Python.
        from naoqi import ALProxy


        with open('/Users/anuj/coursework_cuboulder/spring_2018/algo_hri/poses_random_data0.txt', 'r') as f:

            poseSequence = list(map(int, f.read().split('\n')[:-1]))
        tt=1.0#176.0/len(poseSequence)
        for idx,poseNumber in enumerate(poseSequence):
            self.logger.error(idx)
            if poseNumber == 0:
                self.pose0(tt)
            elif poseNumber == 1:
                self.pose1(tt)
            elif poseNumber == 2:
                self.pose2(tt)
            elif poseNumber == 3:
                self.pose3(tt)
            elif poseNumber == 4:
                self.pose4(tt)
            elif poseNumber == 5:
                self.pose5(tt)
            elif poseNumber == 6:
                self.pose6(tt)
            elif poseNumber == 7:
                self.pose7(tt)
            elif poseNumber == 8:
                self.pose8(tt)
            elif poseNumber == 9:
                self.pose9(tt)

        # activate the output of the box
    pass

def onInput_onStop(self):
    self.onUnload()  # it is recommended to reuse the clean-up as the box is stopped
    self.onStopped()  # activate the output of the box
