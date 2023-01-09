# Collision-Free Trajectory Planning for 3R Robot Manipulator

This project was completed as part of the ME850A course at the Department of Mechanical Engineering at IIT Kanpur, under the supervision of Dr Aninda Chatterjee.

- Collision-free trajectory planning for a 3DOF (degree of freedom) manipulator refers to the process of finding a path for the manipulator to follow that does not result in collisions with any obstacles or other objects in the environment. This is an important consideration in robotic applications, as collisions can cause damage to the manipulator and its surroundings, and can also disrupt the accuracy and precision of the manipulator's movements.

- To plan a collision-free trajectory for a 3DOF manipulator, we need to consider the constraints and limitations of the manipulator, as well as the layout and characteristics of the environment in which it will be operating. This may involve modeling the manipulator and its environment, and using algorithms to search for a path that satisfies the required constraints and avoids collisions.

- Collision avoidance is a related concept that refers to the ability of a manipulator to detect and avoid collisions in real-time, while it is in motion. This can be achieved through the use of sensors, such as lasers or cameras, that can detect the presence and location of obstacles in the environment. The manipulator can then use this information to adjust its trajectory or speed in order to avoid a collision.

- Both collision-free trajectory planning and collision avoidance are important considerations in the design and operation of robotic manipulators, as they help to ensure the safety and reliability of the manipulator, and can also improve its performance and efficiency.

## Objective
- The objective of a project or task is the overall goal or purpose that it is intended to achieve. It is a statement of what is to be accomplished and why it is important. The objective should be clear, specific, and measurable, and it should provide a basis for evaluating the success or effectiveness of the project.

- In the context of the project described in the previous answer, the objective was to design and implement a collision-free trajectory planning algorithm for a 3R robot manipulator. This means that the goal of the project was to create a method for finding a path for the manipulator to follow that avoids collisions with obstacles in the environment. The objective of this project was likely motivated by the importance of ensuring the safety and reliability of the manipulator, and by the need for efficient and accurate navigation in order to achieve the manipulator's desired goals.

## Procedure
The procedure of a project or task refers to the steps or actions that are taken in order to complete it. It outlines the sequence of events that need to happen in order to achieve the project's objectives, and it provides a plan for how the work should be carried out. A procedure should be clear, concise, and easy to follow, and it should include any necessary instructions, guidelines, or requirements.

In the context of the project described in the previous answer, the procedure for designing and implementing a collision-free trajectory planning algorithm for a 3R robot manipulator might include the following steps:

- Define the problem: Clearly identify the goal of the project and the constraints and limitations that need to be considered.
- Research and analysis: Conduct research to gather information about the manipulator, the environment in which it will operate, and the methods and techniques that can be used to plan a collision-free trajectory.
- Design: Develop a plan or approach for generating a collision-free path for the manipulator. This may involve developing a mathematical model or algorithm, or adapting an existing method.
- Implementation: Code or build the algorithm or method in a suitable programming language or software environment.
- Testing: Evaluate the performance of the algorithm or method in simulation or real-world conditions, and make any necessary adjustments or improvements.
- Deployment: Implement the algorithm or method in the manipulator's control system, and test it in real-world conditions to ensure that it is working correctly and efficiently.

## Mathematically
### Cspace:
C-space, or configuration space, is a mathematical representation of the possible configurations or positions that a robot manipulator can assume. It is a high-dimensional space that represents the joint angles or positions of the manipulator's links, and it can be used to analyze the reachability, singularities, and constraints of the manipulator.

To understand the C-space of a robot manipulator, we can start by considering the kinematic model of the manipulator. This model defines the relationship between the joint angles and the position and orientation of the manipulator's end effector (the point at which it can apply forces or perform tasks).

For example, consider a simple 2DOF (degree of freedom) manipulator with two links and two revolute joints. The kinematic model of this manipulator can be represented by a set of forward kinematic equations, which define the position and orientation of the end effector in terms of the joint angles:

$x = l_1cos(q1) + l_2cos(\theta_1 + \theta_2)$

$y = l_1sin(q1) + l_2sin(\theta_1 + \theta_2)$

Where x and y are the coordinates of the end effector, l1 and l2 are the lengths of the links, and q1 and q2 are the joint angles.

The C-space of this manipulator can be represented as a two-dimensional surface in x-y space, with the joint angles q1 and q2 as the coordinates. Each point on this surface corresponds to a unique configuration or position of the manipulator.

In practice, the C-space of a manipulator can be much more complex, with more dimensions and more complex kinematic models. However, the basic concept of using the joint angles as coordinates to represent the manipulator's possible configurations remains the same.

C-space analysis can be used to study the properties and limitations of a manipulator, such as its reachability, singularities, and collision avoidance

### Bspline Curve:
B-spline is a type of curve or surface that is defined by a set of control points and a degree. It is a piecewise polynomial curve that is used to approximate a set of data points or to define a smooth curve or surface through a set of design points.

To understand B-splines, it is helpful to first understand the concept of a polynomial curve. A polynomial curve is a curve that is defined by a polynomial equation, which is an equation of the form:

$y = a_0 + a_1x + a_2x^2 + a3x^3 + \cdots + a_nx^n$

Where y is the dependent variable and x is the independent variable, and the coefficients a0, a1, a2, etc. are constants that determine the shape of the curve.

- A B-spline curve is a piecewise polynomial curve that is defined by a set of control points and a degree. The curve passes through the control points, and the degree determines the smoothness of the curve.

- A B-spline curve is constructed by first dividing the set of control points into a series of segments. Each segment is defined by a set of control points, and a polynomial curve is fit to each segment. The polynomial curves for each segment are then pieced together to form the final B-spline curve.

- To understand how the polynomial curves are fit to the segments, we need to introduce the concept of basis functions. A basis function is a mathematical function that is used to define the shape of a curve or surface. For B-splines, the basis functions are polynomials of a particular degree.

- The polynomial curve for each segment of a B-spline curve is defined as a linear combination of the basis functions for that segment. The coefficients of the basis functions are determined by the control points, and they can be calculated using a process called knot insertion.

- Knot insertion is a method for determining the coefficients of the basis functions in a B-spline curve. It involves solving a system of linear equations, in which the control points are the unknowns and the basis functions are the knowns.

- Once the coefficients of the basis functions have been determined, the polynomial curve for each segment can be calculated. The polynomial curves for all of the segments are then pieced together to form the final B-spline curve

### Controlller:
A PID (proportional-integral-derivative) controller is a control algorithm that is commonly used in trajectory control systems. It is a type of feedback controller that uses the error between the desired trajectory and the actual trajectory to adjust the control signals that are sent to the system.

To understand how a PID controller works, we can start by considering a simple linear system that is being controlled to follow a reference trajectory. The system can be represented by the following mathematical model:

$x = Ax + Bu$

Where x is the state of the system, u is the control input, and A and B are matrices that describe the dynamics of the system.

To control the system to follow a reference trajectory, we need to define a control law that determines the control input u based on the error between the reference trajectory and the actual trajectory. The control law can be represented by the following equation:

$u = -K_pe - K_i\int(e) - K_d*\diff(e)

Where e is the error between the reference trajectory and the actual trajectory, Kp is the proportional gain, Ki is the integral gain, and Kd is the derivative gain. The integral term represents the accumulated error over time, and the derivative term represents the rate of change of the error.

The gains Kp, Ki, and Kd are constants that are chosen to tune the performance of the controller. They determine the relative importance of the proportional, integral, and derivative terms, and they can be adjusted to achieve the desired performance.

To use the PID controller to control the system to follow a reference trajectory, we can define the reference trajectory as the desired state x_desired, and we can use the error e = x_desired - x as the input to the controller. The control input u is then calculated using the control law, and it is applied to the system to adjust the system's behavior.

The PID controller continuously
