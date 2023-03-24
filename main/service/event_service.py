from ..util.db_utils import DBUtils
from ..model.event import Event


class EventService:
    @staticmethod
    def get_all_active_events():
        return Event.query.filter_by(is_completed=False).all()

    @staticmethod
    def create_event(data):
        # TODO - Add validations for event start_time and end_time there should not be
        # any existing active event for home_team or away_team
        event = Event(**data)
        DBUtils.save_to_db(event)
        return event
