# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from mycroft.skills.core import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from mycroft.util.log import LOG

import subprocess

class CallLocalScriptsSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(CallLocalScriptsSkill, self).__init__(name="CallLocalScriptsSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0


    @intent_handler(IntentBuilder("").require("Action").require("What").require("Where"))
    def handle_light_lamp_intent(self, message):
        if message.data["Action"] == "on":
            self.log.debug("On have been discovered")
            if message.data["What"] == "lamp":
                self.log.debug("On and lamp have been discovered")
                if message.data["Where"] == "hall":
                    subprocess.call(['tdtool', '-n 3'])
                    self.speak_dialog("david")
        else: # off
            self.log.debug("Off have been discovered")
            if message.data["What"] == "lamp":
                self.log.debug("On, lamp and hallway have been discovered")
                if message.data["Where"] == "hall":
                    subprocess.call(['tdtool', '-f 3'])
                    self.speak_dialog("david")
                    
                    
    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("Hello").require("World"))
    def handle_hello_world_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("hello.world")

    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    def handle_count_intent(self, message):
        if message.data["Dir"] == "up":
            self.count += 1
        else:  # assume "down"
            self.count -= 1
        self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False


    
def create_skill():
    return CallLocalScriptsSkill()
