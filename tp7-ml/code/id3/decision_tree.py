from collections import Counter
import math
import pandas as pd

class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

class DecisionTree:
    def __init__(self, examples, attributes, parent_examples):
        self.examples = examples
        self.attributes = attributes
        self.parent_examples = parent_examples
        self.root = self.decision_tree_learning(examples, attributes, parent_examples)

    def plurality_value(self, examples):
        classification_counts = Counter(ex['classification'] for ex in examples)
        return classification_counts.most_common(1)[0][0]

    def importance(self, attribute, examples):
        original_entropy = self.entropy(examples)
        weighted_entropy = 0
        for value in set(ex[attribute] for ex in examples):
            subset = [ex for ex in examples if ex[attribute] == value]
            weighted_entropy += len(subset) / len(examples) * self.entropy(subset)
        return original_entropy - weighted_entropy

    def entropy(self,examples):
        class_counts = Counter(ex['classification'] for ex in examples)
        num_examples = len(examples)
        entropy = 0
        for count in class_counts.values():
            p = count / num_examples
            entropy -= p * math.log2(p)
        return entropy

    def decision_tree_learning(self, examples, attributes, parent_examples):
        if not examples:
            return self.plurality_value(parent_examples)
        elif len(set(ex['classification'] for ex in examples)) == 1:
            return examples[0]['classification']
        elif not attributes:
            return self.plurality_value(examples)
        else:
            A = max(attributes, key=lambda a: self.importance(a, examples))
            tree = Node(A)
            for vk in set(ex[A] for ex in examples):
                exs = [ex for ex in examples if ex[A] == vk]
                subtree = self.decision_tree_learning(exs, attributes - {A}, examples)
                tree.children.append((vk, subtree))
            return tree

    def classify(self, example):
        node = self.root
        while isinstance(node, Node):
            vk = example[node.label]
            print(vk)
            for value, subtree in node.children:
                if value == vk:
                    node = subtree
                    
        return node
    
    def print_tree(self, node, depth=0):
        if isinstance(node, Node):
            print('  ' * depth + node.label)
            for value, subtree in node.children:
                print('  ' * (depth+1) + value)
                self.print_tree(subtree, depth+2)
        else:
            print('  ' * depth + str(node))

# Read and prepare data
data = pd.read_csv('./tp7-ml/code/id3/tennis.csv')
data['play'] = data['play'].map({'yes': True, 'no': False})
data['windy'] = data['windy'].map({True: 'True', False: 'False'})

# Cambiamos el nombre de la columna que queremos clasificar
data.rename(columns={'play':'classification'}, inplace=True)

decision_tree = DecisionTree(data.to_dict('records'), set(data.columns) - {'classification'}, [])

decision_tree.print_tree(decision_tree.root)
'''
# Clasificar los datos y agregar una columna con las predicciones
predictions = []
for index, row in data.iterrows():
    prediction = tree.classify(row)
    predictions.append(prediction)
data['prediction'] = predictions

print(data)
'''
