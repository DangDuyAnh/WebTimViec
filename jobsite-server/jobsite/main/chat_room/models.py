# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChatRoom(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_room'


class ChatRoomUser(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    room = models.ForeignKey(ChatRoom, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_room_user'
        unique_together = (('user', 'room'),)


class ChatRoomConversation(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sender_user = models.ForeignKey(ChatRoomUser, models.DO_NOTHING, related_name='sender_user')
    room = models.ForeignKey(ChatRoomUser, models.DO_NOTHING)
    text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_room_conversation'