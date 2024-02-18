import graphviz
import re

dot = graphviz.Digraph(comment="Flowz", format='png')
dot 


input_data = '''
## Opening Activity:
To begin our exploration of the topic of Gravitation, we will start with an engaging and interactive activity called "Apple Investigation." Students will be asked to observe an apple suspended from a string and predict what would happen if the string is cut. This activity will help activate prior knowledge by tapping into students' experiences with gravity in their daily lives, and spark curiosity by introducing the concept of gravitational force in a relatable way.

## Instructional Activities:
1. *Lab Experiment:* Students can be divided into groups for conducting experiments to observe the effects of gravity on objects. Each group can investigate different objects with varying masses and distances from the ground. This hands-on activity will cater to kinesthetic learners, and provide opportunities for students to collaborate and problem solve.
2. *Interactive Demonstrations:* Incorporating multimedia tools such as videos, simulations, and interactive whiteboards can help deliver content in a visually engaging way for visual learners. For example, we could use a gravity simulator that allows students to manipulate variables and observe the effects on the gravitational force between two masses.
3. *Guided Discussions:* Teachers can facilitate small group discussions where students share their observations and interpretations of experiments or videos related to gravitation. This will cater to verbal learners, and provide opportunities for students to develop critical thinking skills through collaborative problem-solving.

## Practice Activities:
1. *Open-ended Question:* "Explain how the force of gravity keeps planets in their orbits around stars."
2. *Multiple Choice:* "Which of the following best describes the behavior of two objects under the influence of gravity? A) They repel each other B) They attract each other C) They have no effect on each other"
3. *Short Answer:* "Describe how the weight of an object affects its acceleration due to gravity."
4. *Calculation:* "If a 2 kg mass is placed 5 meters above the ground, calculate the force of gravity acting on it."
5. *Design Challenge:* "Design and build a simple Rube Goldberg machine that demonstrates the concept of potential energy and gravitational forces."

## Assessment:
1. *Formative:* Ongoing assessments through class discussions, observations during experiments, and informal quizzes can help teachers evaluate students' understanding and identify areas where additional support may be needed.
2. *Summative:* A formal assessment could be in the form of a test that includes multiple choice questions, short answers, and open-ended responses to assess students' comprehension of key concepts related to gravitation.

## Differentiation:
1. *Extension:* For advanced learners, teachers can provide additional resources such as research projects, complex simulations, or challenging design tasks to deepen their understanding of the topic.
2. *Modified Instructions:* For English language learners or students with learning disabilities, providing visual aids, simplified instructions, and extra time on assignments can help ensure they have equal opportunities to demonstrate their knowledge.
3. *Small Group Instruction:* Providing small group instruction for students who struggle with the topic can help address individual needs through targeted interventions and personalized feedback.
'''
arr = []
paras = input_data.split('\n\n')

for e,para in enumerate(paras):
    headi = re.findall(r'##\s+(.*):', para)
    lower = re.findall(r'. \*(.*):\*', para)
    arr.append(headi)
    arr[e].append(lower)

# Connect parent nodes to other parent nodes
for i, parent1 in enumerate(arr[:-1]):
    for parent2 in arr[i+1:]:
        dot.edge(parent1[0], parent2[0])

# Create child nodes and connect them to their parent nodes
for parent in arr:
    for child in parent[1]:
        dot.node(child)
        dot.edge(parent[0], child)

# Save the flowchart as a PNG image
dot.render('flowchart', view=True)
