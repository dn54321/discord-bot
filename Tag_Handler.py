from abc import ABC, abstractmethod
import discord
from properties import *
class Tag_Handler:
    def __init__(self, state, *argv):
        self.state = state
        self.argv = argv
    async def run(self, client, payload):
        await self.state.prep(client, payload, *self.argv)


class Add_Role:
    def __init__(self):
        self.reqs = []    # requires that this role is in member.
        self.notreqs = [] # requires that this role is not in member.
        self.role = []    # role to obtain if any.
    async def prep(self, client, payload, *argv):
        emote = argv[0]
        msg_id = argv[1]
        argv = argv[2:]
        await self.run(client, emote, msg_id, payload, *argv)
        
    async def run(self, client, emote, msg_id, payload, *argv):
        if not self.role:
            for arg in argv:
                if arg[0] == '-': # Must not have this role
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg[1:])
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.notreqs.append(role)
                elif arg[0] == '+': # Role that you will obtain if this succeeds
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg[1:])
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.role.append(role)
                else: # Must have this role
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg)
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.reqs.append(role)
            if not self.role:
                raise Exception("No roles to obtain when getting this role.")
        member = client.get_guild(GUILD).get_member(payload.user_id)
        roles = member.roles
        if set(self.reqs).issubset(member.roles) and not [i for i in self.notreqs if i in member.roles]:
            await member.add_roles(*self.role)

class Remove_Role:
    def __init__(self):
        self.reqs = []    # requires that this role is in member.
        self.notreqs = [] # requires that this role is not in member.
        self.role = []    # role to obtain if any.
    async def prep(self, client, payload, *argv):
        emote = argv[0]
        msg_id = argv[1]
        argv = argv[2:]
        await self.run(client, emote, msg_id, payload, *argv)
        
    async def run(self, client, emote, msg_id, payload, *argv):
        if not self.role:
            for arg in argv:
                if arg[0] == '-': # Must not have this role
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg[1:])
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.notreqs.append(role)
                elif arg[0] == '+': # Role that you will obtain if this succeeds
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg[1:])
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.role.append(role)
                else: # Must have this role
                    role = discord.utils.get(client.get_guild(GUILD).roles, name=arg)
                    if role is None: 
                        raise Exception("Role: " + arg[1:] + " does not exist")
                    self.reqs.append(role)
            if not self.role:
                raise Exception("No roles to obtain when getting this role.")
        member = client.get_guild(GUILD).get_member(payload.user_id)
        roles = member.roles
        if set(self.reqs).issubset(member.roles) and not [i for i in self.notreqs if i in member.roles]:
            await member.remove_roles(*self.role)

class addRoleUpTo:
    pass


