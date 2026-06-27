class Optimization:

    @staticmethod
    def evaluate_solution(assignments):

        score = 100

        faculty_load = {}

        for item in assignments:

            faculty = item["faculty"]

            faculty_load[faculty] = (
                faculty_load.get(faculty, 0) + 1
            )

        for load in faculty_load.values():

            if load > 3:
                score -= 10

        return {
            "quality_score": score,
            "faculty_distribution": faculty_load
        }