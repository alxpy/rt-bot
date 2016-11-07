from elasticmagic import Document
from elasticmagic import Field
from elasticmagic.types import Integer
from elasticmagic.types import String


class MessageDocument(Document):
    __doc_type__ = 'message'

    __mapping_options__ = {
        'dynamic': True,
        'date_detection': False,
    }

    user_id = Field(Integer)
    user_name = Field(String)
    text = Field(String)
