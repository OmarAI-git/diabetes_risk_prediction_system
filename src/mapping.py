class MappingData():

  def __init__(self, user_data: dict):
    self.user_data = user_data
    self.user_output = None

  def _mapping_GenHlth(self, num):
    if num == 'excellent':
      return 1
    elif num == 'very good':
      return 2
    elif num == 'good':
      return 3
    elif num == 'fair':
      return 4
    else:
      return 5


  def _mapping_age(self, age):
    if age <= 24:
      return 1
    elif age <= 29:
      return 2
    elif age <= 34:
      return 3
    elif age <= 39:
      return 4
    elif age <= 44:
      return 5
    elif age <= 49:
      return 6
    elif age <= 54:
      return 7
    elif age <= 59:
      return 8
    elif age <= 64:
      return 9
    elif age <= 69:
      return 10
    elif age <= 74:
      return 11
    elif age <= 79:
      return 12
    else:
      return 13



  def mapping_data(self):
    self.user_output = {}

    if self.user_data['HighBP'] == 'No high BP':
      self.user_output['HighBP'] = 0
    else:
      self.user_output['HighBP'] = 1

    if self.user_data['HighChol'] == 'No high cholesterol':
      self.user_output['HighChol'] = 0
    else:
      self.user_output['HighChol'] = 1

    if self.user_data['CholCheck'] == 'No cholesterol check':
      self.user_output['CholCheck'] = 0
    else:
      self.user_output['CholCheck'] = 1

    self.user_output['BMI'] = self.user_data['BMI']

    if self.user_data['Smoker'] == 'No':
      self.user_output['Smoker'] = 0
    else:
      self.user_output['Smoker'] = 1

    if self.user_data['Stroke'] == 'No':
      self.user_output['Stroke'] = 0
    else:
      self.user_output['Stroke'] = 1

    if self.user_data['HeartDiseaseorAttack'] == 'No':
      self.user_output['HeartDiseaseorAttack'] = 0
    else:
      self.user_output['HeartDiseaseorAttack'] = 1

    if self.user_data['PhysActivity'] == 'No':
      self.user_output['PhysActivity'] = 0
    else:
      self.user_output['PhysActivity'] = 1

    if self.user_data['Fruits'] == 'No':
      self.user_output['Fruits'] = 0
    else:
      self.user_output['Fruits'] = 1

    if self.user_data['Veggies'] == 'No':
      self.user_output['Veggies'] = 0
    else:
      self.user_output['Veggies'] = 1

    if self.user_data['HvyAlcoholConsump'] == 'No':
      self.user_output['HvyAlcoholConsump'] = 0
    else:
      self.user_output['HvyAlcoholConsump'] = 1

    if self.user_data['AnyHealthcare'] == 'No':
      self.user_output['AnyHealthcare'] = 0
    else:
      self.user_output['AnyHealthcare'] = 1

    if self.user_data['NoDocbcCost'] == 'No':
      self.user_output['NoDocbcCost'] = 0
    else:
      self.user_output['NoDocbcCost'] = 1

    if self.user_data['NoDocbcCost'] == 'No':
      self.user_output['NoDocbcCost'] = 0
    else:
      self.user_output['NoDocbcCost'] = 1

    self.user_output['GenHlth'] = self._mapping_GenHlth(self.user_data['GenHlth'])

    self.user_output['MentHlth'] = self.user_data['MentHlth']

    self.user_output['PhysHlth'] = self.user_data['PhysHlth']

    if self.user_data['DiffWalk'] == 'No':
      self.user_output['DiffWalk'] = 0
    else:
      self.user_output['DiffWalk'] = 1

    if self.user_data['Sex'] == 'Female':
      self.user_output['Sex'] = 0
    else:
      self.user_output['Sex'] = 1

    self.user_output['Age'] = self._mapping_age(self.user_data['Age'])

    return self.user_output
