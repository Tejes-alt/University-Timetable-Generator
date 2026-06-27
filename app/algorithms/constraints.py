class Constraints:

    @staticmethod
    def faculty_conflict(assignments, faculty, timeslot):
        for item in assignments:
            if (
                item["faculty"] == faculty and
                item["timeslot"] == timeslot
            ):
                return True
        return False

    @staticmethod
    def room_conflict(assignments, room, timeslot):
        for item in assignments:
            if (
                item["room"] == room and
                item["timeslot"] == timeslot
            ):
                return True
        return False

    @staticmethod
    def section_conflict(assignments, section, timeslot):
        for item in assignments:
            if (
                item["section"] == section and
                item["timeslot"] == timeslot
            ):
                return True
        return False