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
