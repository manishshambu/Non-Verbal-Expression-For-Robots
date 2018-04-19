// add sources

import ddf.minim.*;
import ddf.minim.ugens.*;

String dir = "/Users/anuj/coursework_cuboulder/spring_2018/algo_hri/skeleton/";

Minim minim;

AudioInput in;
AudioRecorder recorder;
boolean recorded;
boolean start_capture = false;

// for playing back
AudioOutput out;
FilePlayer player;

int trial = -1;

int m;

import SimpleOpenNI.*;
import java.util.Arrays;
 int startTime;


// create kinect object
SimpleOpenNI  kinect;
// image storage from kinect
PImage kinectDepth;
PImage kinectImg;
// int of each user being  tracked
int[] userID;
int frame = -1;
// user colors
color[] userColor = new color[]{ color(255,0,0), color(0,255,0), color(0,0,255),
                                 color(255,255,0), color(255,0,255), color(0,255,255)};
 
 
JSONObject json;
JSONArray json_out_real = new JSONArray();
JSONArray json_out_proj = new JSONArray();

// postion of head to draw circle
PVector headPosition = new PVector();
PVector neckPosition = new PVector();
PVector leftShoulderPosition = new PVector();
PVector rightShoulderPosition = new PVector();
PVector leftElbowPosition = new PVector();
PVector rightElbowPosition = new PVector();
PVector leftHandPosition = new PVector();
PVector rightHandPosition = new PVector();
PVector torsoPosition = new PVector();
PVector leftHipPosition = new PVector();
PVector rightHipPosition = new PVector();
PVector leftKneePosition = new PVector();
PVector rightKneePosition = new PVector();
PVector leftFootPosition = new PVector();
PVector rightFootPosition = new PVector();

// turn headPosition into scalar form
float distanceScalar;
// diameter of head drawn in pixels
float headSize = 200;
 
// threshold of level of confidence
float confidenceLevel = 0.5;
// the current confidence level that the kinect is tracking
float confidence;
// vector of tracked head for confidence checking
PVector confidenceVector = new PVector();
 
/*---------------------------------------------------------------
Starts new kinect object and enables skeleton tracking.
Draws window
----------------------------------------------------------------*/
void setup()
{
    // start a new kinect object
    kinect = new SimpleOpenNI(this);
    kinect.enableRGB();
    // enable depth sensor
    kinect.enableDepth();

    // enable skeleton generation for all joints
    kinect.enableUser();

    // draw thickness of drawer
    strokeWeight(3);
    // smooth out drawing
    smooth();

    // create a window the size of the depth information
    size(kinect.depthWidth()*2, kinect.depthHeight());

    // AUDIO //

    //size(512, 200, P3D);

    minim = new Minim(this);

    // get a stereo line-in: sample buffer length of 2048
    // default sample rate is 44100, default bit depth is 16
    in = minim.getLineIn(Minim.STEREO, 2048);
    trial=trial+1;
recorder = minim.createRecorder(in, dir+trial+"/myrecording.wav");

    // get an output we can playback the recording on
    out = minim.getLineOut( Minim.STEREO );
} // void setup()

void keyReleased()
{
    if (key == 'r' ) 
    {
        // to indicate that you want to start or stop capturing audio data, 
        // you must callstartRecording() and stopRecording() on the AudioRecorder object. 
        // You can start and stop as many times as you like, the audio data will 
        // be appended to the end of to the end of the file. 
        if ( recorder.isRecording() ) 
        {
            recorder.endRecord();
            start_capture = false;
            if ( player != null )
            {
                player.unpatch( out );
                player.close();
            }
            player = new FilePlayer( recorder.save() );
            //player.patch( out );

            //recorded = true;
            
            frame=-1;
            trial=trial+1;
            recorder = minim.createRecorder(in, dir+trial+"/myrecording.wav");

        }
        else 
        {
            // create an AudioRecorder that will record from in to the filename specified.
            // the file will be located in the sketch's main folder.
            
            recorder.beginRecord();
            start_capture = true;
            startTime = millis();
        }
    }
}
 
/*---------------------------------------------------------------
Updates Kinect. Gets users tracking and draws skeleton and
head if confidence of tracking is above threshold
----------------------------------------------------------------*/
void draw(){
    // update the camera
    kinect.update();
    // get Kinect data
    kinectDepth = kinect.depthImage();
    kinectImg = kinect.rgbImage();
    // draw depth image at coordinates (0,0)
    image(kinectDepth,0,0); 
    image(kinectImg, kinectDepth.width, 0);

    // get all user IDs of tracked users
    userID = kinect.getUsers();

    // loop through each user to see if tracking
    for(int i=0;i<userID.length;i++)
    {
        // if Kinect is tracking certain user then get joint vectors
        if(kinect.isTrackingSkeleton(userID[i]))
        {
            // get confidence level that Kinect is tracking head
            confidence = kinect.getJointPositionSkeleton(userID[i],
            SimpleOpenNI.SKEL_HEAD,confidenceVector);

            // if confidence of tracking is beyond threshold, then track user
            if(confidence > confidenceLevel)
            {
                // change draw color based on hand id#
                stroke(userColor[(i)]);
                // fill the ellipse with the same color
                fill(userColor[(i)]);
                // draw the rest of the body
                drawSkeleton(userID[i]);
            } //if(confidence > confidenceLevel)
        } //if(kinect.isTrackingSkeleton(userID[i]))
    } //for(int i=0;i<userID.length;i++)
} // void draw()
 //SAVE SKELETON WITH DEPTH
/*---------------------------------------------------------------
Draw the skeleton of a tracked user.  Input is userID
----------------------------------------------------------------*/

//Add a PVector as a string representation of a float array to a JSON object
void setVector(JSONObject json, String attributeName, PVector v) {
    json.setString( attributeName, Arrays.toString( new float[]{ v.x, v.y, v.z} ) );
}

void drawSkeleton(int userId){
      //draw limb from head to neck
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_HEAD, SimpleOpenNI.SKEL_NECK);
    //draw limb from neck to left shoulder
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_LEFT_SHOULDER);
    //draw limb from left shoulde to left elbow
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_LEFT_ELBOW);
    //draw limb from left elbow to left hand
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_ELBOW, SimpleOpenNI.SKEL_LEFT_HAND);
    //draw limb from neck to right shoulder
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_NECK, SimpleOpenNI.SKEL_RIGHT_SHOULDER);
    //draw limb from right shoulder to right elbow
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_RIGHT_ELBOW);
    //draw limb from right elbow to right hand
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW, SimpleOpenNI.SKEL_RIGHT_HAND);
    //draw limb from left shoulder to torso
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, SimpleOpenNI.SKEL_TORSO);
    //draw limb from right shoulder to torso
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, SimpleOpenNI.SKEL_TORSO);
    //draw limb from torso to left hip
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_LEFT_HIP);
    //draw limb from left hip to left knee
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_HIP,  SimpleOpenNI.SKEL_LEFT_KNEE);
    //draw limb from left knee to left foot
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_LEFT_KNEE, SimpleOpenNI.SKEL_LEFT_FOOT);
    //draw limb from torse to right hip
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_TORSO, SimpleOpenNI.SKEL_RIGHT_HIP);
    //draw limb from right hip to right knee
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_HIP, SimpleOpenNI.SKEL_RIGHT_KNEE);
    //draw limb from right kneee to right foot
    kinect.drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_KNEE, SimpleOpenNI.SKEL_RIGHT_FOOT);
    
    
    // get 3D position of head
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_HEAD,headPosition);
    // convert real world point to projective space
    //??kinect.convertRealWorldToProjective(headPosition,headPosition);
    // create a distance scalar related to the depth in z dimension
    //distanceScalar = (525/headPosition.z);
    // draw the circle at the position of the head with the head size scaled by the distance scalar
    //ellipse(headPosition.x,headPosition.y, distanceScalar*headSize,distanceScalar*headSize);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_NECK, neckPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER, leftShoulderPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER, rightShoulderPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_ELBOW, leftElbowPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW, rightElbowPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_HAND, leftHandPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_HAND, rightHandPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_TORSO, torsoPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_HIP, leftHipPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_HIP, rightHipPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_KNEE, leftKneePosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_KNEE, rightKneePosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_LEFT_FOOT, leftFootPosition);
    kinect.getJointPositionSkeleton(userId, SimpleOpenNI.SKEL_RIGHT_FOOT, rightFootPosition);
    //JSONObject json = new JSONObject();
    
    

    if (start_capture) {
        frame = frame+1;
        //int time_ms = millis()-startTime;
        json = new JSONObject();
        setVector(json, "head", headPosition);
        setVector(json, "neck", neckPosition);
        setVector(json, "leftShoulder", leftShoulderPosition);
        setVector(json, "rightShoulder", rightShoulderPosition);
        setVector(json, "leftElbow", leftElbowPosition);
        setVector(json, "rightElbow", rightElbowPosition);
        setVector(json, "leftHand", leftHandPosition);
        setVector(json, "rightHand", rightHandPosition);
        setVector(json, "torso", torsoPosition);
        setVector(json, "leftHip", leftHipPosition);
        setVector(json, "rightHip", rightHipPosition);
        setVector(json, "leftKnee", leftKneePosition);
        setVector(json, "rightKnee", rightKneePosition);
        setVector(json, "leftFoot", leftFootPosition);
        setVector(json, "rightFoot", rightFootPosition);
        json.setInt("time_ms", millis()-startTime);
        json_out_real.setJSONObject(frame, json);
        saveJSONArray(json_out_real, dir+trial+"/realWorldCoords.json");
        
        kinect.convertRealWorldToProjective(headPosition,headPosition);
        kinect.convertRealWorldToProjective(neckPosition,neckPosition);
        kinect.convertRealWorldToProjective(leftShoulderPosition,leftShoulderPosition);
        kinect.convertRealWorldToProjective(rightShoulderPosition,rightShoulderPosition);
        kinect.convertRealWorldToProjective(leftElbowPosition,leftElbowPosition);
        kinect.convertRealWorldToProjective(rightElbowPosition,rightElbowPosition);
        kinect.convertRealWorldToProjective(leftHandPosition,leftHandPosition);
        kinect.convertRealWorldToProjective(rightHandPosition,rightHandPosition);
        kinect.convertRealWorldToProjective(torsoPosition,torsoPosition);
        kinect.convertRealWorldToProjective(leftHipPosition,leftHipPosition);
        kinect.convertRealWorldToProjective(rightHipPosition,rightHipPosition);
        kinect.convertRealWorldToProjective(leftKneePosition,leftKneePosition);
        kinect.convertRealWorldToProjective(rightKneePosition,rightKneePosition);
        kinect.convertRealWorldToProjective(leftFootPosition,leftFootPosition);
        kinect.convertRealWorldToProjective(rightFootPosition,rightFootPosition);

        json = new JSONObject();
        setVector(json, "head", headPosition);
        setVector(json, "neck", neckPosition);
        setVector(json, "leftShoulder", leftShoulderPosition);
        setVector(json, "rightShoulder", rightShoulderPosition);
        setVector(json, "leftElbow", leftElbowPosition);
        setVector(json, "rightElbow", rightElbowPosition);
        setVector(json, "leftHand", leftHandPosition);
        setVector(json, "rightHand", rightHandPosition);
        setVector(json, "torso", torsoPosition);
        setVector(json, "leftHip", leftHipPosition);
        setVector(json, "rightHip", rightHipPosition);
        setVector(json, "leftKnee", leftKneePosition);
        setVector(json, "rightKnee", rightKneePosition);
        setVector(json, "leftFoot", leftFootPosition);
        setVector(json, "rightFoot", rightFootPosition);
        json.setInt("time_ms", millis()-startTime);
        json_out_proj.setJSONObject(frame, json);
        saveJSONArray(json_out_proj, dir+trial+"/projSpaceCoords.json");

        save(dir+trial+"/frames/"+frame+".jpg");
    }
} // void drawSkeleton(int userId)
 
/*---------------------------------------------------------------
When a new user is found, print new user detected along with
userID and start pose detection.  Input is userID
----------------------------------------------------------------*/
void onNewUser(SimpleOpenNI curContext, int userId){
    println("New User Detected - userId: " + userId);
    // start tracking of user id
    curContext.startTrackingSkeleton(userId);
}
