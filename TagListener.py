import discord

# An event listener which fires when a message is tagged with an emote.
class TagListener(discord.Client):
    # Accepts many event handlers of object tagHandler.
    # @client - the client of the discord-bot.
    # @onTag - A list of objects which fire when a user reacts to a message.
    # @offTag - A list of objects which fire when a user unreacts to a message.
    # @orTag - A list of objects which fire when either a message is reacted or unreacted to.
    def __init__(self):
        self.onTag = []
        self.offTag = []  

    # @event - An event object tagHandler.
    # @location - A string that specifies when the tagHandler should fire.
    #           - location is either "onTag", "offTag".
    def add_event(self, event, location):
        """Adds an object tagHandler for the object to be handled by."""
        if location is "onTag":
            self.onTag.append(event)
        elif location is "offTag":
            self.offTag.append(event)
        else:
            raise Exception('location not valid') # debugging purposes

    # @event - An event object tagHandler.
    # @location - An optional string that specifies where the tagHandler is
    #           - location is either "onTag", "offTag".
    def remove_Event(self, event, location):
        """Removes an object tagHandler from the class"""
        if location is "onTag":
            self.onTag.remove(event)
        elif location is "offTag":
            self.offTag.remove(event)
        else:
            raise Exception('location not valid') # debugging purposes

    
    # for a better understanding of payload: https://discordpy.readthedocs.io/en/latest/api.html#discord.RawReactionActionEvent

    # Whenever someone reacts to a message, this function will fire.
    async def on_raw_reaction_add(self, payload):
        for event in self.onTag:
            event.run(payload, self) 
    # Whenver someone unreacts to a message, this function will fire.
    async def on_raw_reaction_remove(self, payload):
        for event in self.onTag:
            event.run(payload, self) 