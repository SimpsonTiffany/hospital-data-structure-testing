# Doctor Reporting Tree & Emergency Queue

This assignment simulates a medical management system built using non-linear data structures. It includes a custom binary tree to model a doctor reporting hierarchy and a min-heap to manage patient urgency in an emergency room queue. The project reinforces recursive logic, priority-based operations, and tree traversal techniques.

## Doctor Reporting Tree

### DoctorNode Class
Represents a doctor in the reporting hierarchy.

**Attributes**
- `name` (str): The doctor’s name
- `left` (DoctorNode or None): Reference to the left report
- `right` (DoctorNode or None): Reference to the right report

### DoctorTree Class
Manages the binary tree structure of doctor reports.

**Attributes**
- `root` (DoctorNode or None): Reference to the root doctor

**Methods**
- `insert(parent_name, doctor_name, side)`
- `preorder(node)`
- `inorder(node)`
- `postorder(node)`

Each traversal method demonstrates a different way of processing hierarchical data.

## Emergency Priority Queue

### Patient Class
Represents a patient waiting for emergency care.

**Attributes**
- `name` (str): The patient’s name
- `urgency` (int): A score from 1 to 10, where 1 is most urgent

### MinHeap Class
Manages patients using a priority queue based on urgency.

**Methods**
- `insert(patient)`
- `remove_min()`
- `peek()`
- `print_heap()`

The heap always serves the most urgent patient first.

## How to Run
Run each file individually using Python:

```bash
python doctor_tree.py
python emergency_queue.py

## Design Reflection

A binary tree is an appropriate data structure for the doctor reporting system because it naturally represents hierarchical relationships. Each doctor may have up to two direct reports, which aligns well with a left and right child structure. Using a tree allows the hierarchy to grow dynamically and supports recursive traversal, making it easier to search for a specific doctor or display the structure in different ways. Compared to flat data structures like lists or dictionaries, a tree provides a clearer and more intuitive representation of reporting relationships in an organizational setting.

Traversal methods serve different real-world purposes depending on the reporting or workflow needs. Preorder traversal is useful when information should be processed from leadership down, such as generating a command or announcement starting with senior doctors. Inorder traversal can be helpful when displaying doctors in a structured or alphabetical-like sequence when the tree is organized logically. Postorder traversal is valuable when actions need to be completed from the lowest level upward, such as evaluating performance or removing doctors from the system after their reports have been handled.

A min-heap is ideal for modeling emergency room intake because it prioritizes patients based on urgency rather than arrival order. By always keeping the most urgent patient at the root, the system ensures that critical cases are handled first. Heap operations allow insertions and removals to remain efficient even as the number of patients grows, closely simulating the real-time decision-making required in emergency medical environments.

