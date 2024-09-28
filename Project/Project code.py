class Fan:
    def _init_(self, fan_id, name, email):
        self.fan_id = fan_id
        self.name = name
        self.email = email


class FanManager:
    def _init_(self):
        self.fans = {}

    def add_fan(self, fan):
        self.fans[fan.fan_id] = fan

    def get_fan(self, fan_id):
        return self.fans.get(fan_id)

    def update_fan(self, fan):
        if fan.fan_id in self.fans:
            self.fans[fan.fan_id] = fan
            return True
        return False

    def delete_fan(self, fan_id):
        if fan_id in self.fans:
            del self.fans[fan_id]
            return True
        return False


class Survey:
    def _init_(self, survey_id, questions=None):
        self.survey_id = survey_id
        self.questions = questions or []
        self.responses = {}

    def add_question(self, question):
        self.questions.append(question)

    def conduct_survey(self, fan_id, responses):
        if len(responses) != len(self.questions):
            raise ValueError("Responses must match the number of questions.")
        self.responses[fan_id] = responses

    def get_responses(self):
        return self.responses


class SurveyManager:
    def _init_(self):
        self.surveys = {}

    def create_survey(self, survey):
        self.surveys[survey.survey_id] = survey

    def find_survey(self, survey_id):
        return self.surveys.get(survey_id)

    def delete_survey(self, survey_id):
        if survey_id in self.surveys:
            del self.surveys[survey_id]
            return True
        return False


class ReportManager:
    def _init_(self, survey_manager, fan_manager):
        self.survey_manager = survey_manager
        self.fan_manager = fan_manager

    def generate_report(self, survey_id):
        survey = self.survey_manager.find_survey(survey_id)
        if not survey:
            return "Survey not found."
        
        total_fans = len(self.fan_manager.fans)
        total_responses = len(survey.responses)

        response_rate = total_responses / total_fans if total_fans > 0 else 0

        return {
            "report_id": survey_id,
            "response_rate": response_rate,
            "responses": survey.responses
        }


# Example Usage
fan_manager = FanManager()
survey_manager = SurveyManager()

# Adding fans
fan1 = Fan(1, "Alice", "alice@example.com")
fan2 = Fan(2, "Bob", "bob@example.com")

fan_manager.add_fan(fan1)
fan_manager.add_fan(fan2)

# Creating a survey
survey = Survey("survey1", questions=["How satisfied are you?", "What can we improve?"])
survey_manager.create_survey(survey)

# Conducting the survey
survey.conduct_survey(1, ["Very satisfied", "More events"])
survey.conduct_survey(2, ["Satisfied", "Better communication"])

# Generating report
report_manager = ReportManager(survey_manager, fan_manager)
report = report_manager.generate_report("survey1")
print(report)