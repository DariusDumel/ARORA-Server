from django.db import models
from UserInfos.models import UserInfo
from Quests.models import QuestReport
from Notifications.models import Notification

class UserInteractionType(models.Model):
    user_interaction_type_id = models.AutoField(primary_key=True, db_column='UserInteractionTypeId')  # Primary Key
    user_interaction_description = models.TextField(db_column='UserInteractionTypeDescription')

    def __int__(self):
        return self.user_interaction_type_id


# Create your models here.
class UserInteraction(models.Model):
    user_interaction_id = models.AutoField(primary_key=True, db_column='UserInteractionId')  # Primary Key
    user_interaction_created_at = models.DateTimeField(auto_now=True, db_column='UserInteractionCreatedAt')

    # Foreign Key, UserInfo:UserId -> UserInteraction:InitiatorUserId
    initiator_user_id = models.ForeignKey(UserInfo, related_name='initiator', on_delete=models.CASCADE,
                                          db_column='InitiatorUserId')

    # Foreign Key, UserInfo:UserId -> UserInteraction:ReceiverUserId
    receiver_user_id = models.ForeignKey(UserInfo, related_name='receiver', on_delete=models.CASCADE,
                                         db_column='ReceiverUserId')

    user_interaction_type_id = models.ForeignKey(UserInteractionType, on_delete=models.CASCADE,
                                                 db_column='UserInteractionTypeId')
    user_interaction_content = models.TextField(db_column='UserInteractionContent')

    # Need a field for a QuestReportID to which this interaction corresponds
    #quest_report_id = models.ForeignKey(QuestReport, on_delete=models.CASCADE, 
    #                                             db_column='QuestReportId', blank=True, 
    #                                             null=True, unique=False, editable=True)

    # Need a field for a Notification to which this interaction corresponds
    notification_id = models.ForeignKey(Notification, on_delete=models.CASCADE, 
                                                 db_column='NotificationId', blank=True, 
                                                 null=True, unique=False, editable=True)

    # Need a field for a QuestReportID to which this interaction corresponds
    #notification_id = models.ForeignKey(, on_delete=models.CASCADE, db_column='QuestReportId', default=1, unique=False, editable=True)


    def __str__(self):
        return self.user_interaction_content
