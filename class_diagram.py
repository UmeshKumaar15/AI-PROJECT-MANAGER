
from graphviz import Digraph

dot = Digraph(comment='Class Diagram for ASL Recognition and Tutoring Mobile Application')

# Classes
dot.node('ASLRecognitionAndTutoring', 'ASL Recognition and Tutoring\nMobile Application')
dot.node('RealTimeASLRecognition', 'Real-time ASL\nRecognition')
dot.node('InteractiveLearningModules', 'Interactive Learning\nModules')
dot.node('UserProgressTracking', 'User Progress\nTracking')
dot.node('OfflineASLDictionary', 'Offline ASL\nDictionary')
dot.node('DeepLearningModel', 'Deep Learning\nModel')
dot.node('Camera', 'Camera')
dot.node('Database', 'Database')
dot.node('UserInterface', 'User Interface')

# Relationships
dot.edge('ASLRecognitionAndTutoring', 'RealTimeASLRecognition')
dot.edge('ASLRecognitionAndTutoring', 'InteractiveLearningModules')
dot.edge('ASLRecognitionAndTutoring', 'UserProgressTracking')
dot.edge('ASLRecognitionAndTutoring', 'OfflineASLDictionary')
dot.edge('RealTimeASLRecognition', 'DeepLearningModel')
dot.edge('RealTimeASLRecognition', 'Camera')
dot.edge('InteractiveLearningModules', 'UserInterface')
dot.edge('UserProgressTracking', 'Database')
dot.edge('OfflineASLDictionary', 'Database')
dot.edge('UserInterface', 'Camera')

# Save the diagram to a png file
dot.render('/Users/s.sanjithsuryasrinivasan/CAPSTONE_mybranch/AI-PROJECT-MANAGER/backend/static/class_diagram.png', view=True) 
