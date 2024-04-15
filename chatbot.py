import random
import re

class FriendChat:
    negative_responses = ["no", "nope", "nah", "not really", "sorry"]
    exit_commands = ["quit", "pause", "exit", "bye", "goodbye", "see you later"]

    random_questions = [
        "What's up?",
        "How's your day going?",
        "Got any plans for the weekend?",
        "Do you believe in aliens?",
        "What's your favorite movie?",
        "Have you tried any new hobbies lately?",
        "Do you prefer coffee or tea?",
        "What's the best vacation you've ever taken?",
        "If you could travel anywhere in the world, where would you go?",
    ]

    def __init__(self):
        self.conversation_rules = {
            "describe_planet_intent": r".*\s*tell me about your planet.*",
            "answer_why_intent": r"why\sare.*",
            "about_intellipaat": r".*\s*what is intellipaat.*",
        }

    def greet(self):
        self.name = input("Hey there! What's your name?\n")
        will_help = input(f"Hi {self.name}, want to chat?\n")
        if will_help.lower() in self.negative_responses:
            print("No worries, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        return any(reply.lower() == command for command in self.exit_commands)

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        found_match = False
        for intent, regex_pattern in self.conversation_rules.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                break

        if found_match and intent == "describe_planet_intent":
            return self.describe_planet_intent()
        elif found_match and intent == "answer_why_intent":
            return self.answer_why_intent()
        elif found_match and intent == "about_intellipaat":
            return self.about_intellipaat()
        elif not found_match:
            return self.no_match_intent()

    def describe_planet_intent(self):
        responses = [
            "My planet is a utopia of diverse organisms.",
            "Our planet is known for its breathtaking landscapes and vibrant culture.",
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = [
            "I'm just here to hang out and chat with you.",
            "I love learning about new things, like your planet!",
            "I heard Earth is a cool place to visit, so I came here.",
        ]
        return random.choice(responses)

    def about_intellipaat(self):
        responses = [
            "Intellipaat is a leading professional educational company.",
            "It offers a wide range of courses to help you grow your skills.",
            "With Intellipaat, learning is fun and effective!",
        ]
        return random.choice(responses)

    def no_match_intent(self):
        responses = [
            "Tell me more about that!",
            "I'm curious, can you elaborate?",
            "That's interesting, I'd love to hear more.",
            "Why do you think that is?",
            "I see. How does that make you feel?",
        ]
        return random.choice(responses)

chat = FriendChat()
chat.greet()
