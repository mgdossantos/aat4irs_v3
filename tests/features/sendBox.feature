Feature: Send box according to the box color to the target with the same color
  As a operator,
  I want to send the box with a specific color to the the delivery point using the robot
  So that I can automate the process using a industrial robotic system



  Scenario: Move the box with a specific color from conveyor to the target with the same color
    Given the industrial robotic system is initialized
    And the conveyor is initialized
    And the robot is at home with the position error threshold being less than or equal "0.02" cm in the x-axis
    And the robot is at home with the position error threshold being less than or equal "0.02" cm in the y-axis
    And the robot is at home with the position error threshold being less than or equal "0.02" cm in the z-axis
    And the box is in the conveyor with the position error threshold being less than or equal "0.01" cm in the x-axis
    And the box is in the conveyor with the position error threshold being less than or equal "0.01" cm in the y-axis
    And the box is in the conveyor with the position error threshold being less than or equal "0.01" cm in the z-axis
    When the pick-and-place finished
    Then the box should be in the specific target with the position error threshold being less than or equal "0.35" cm in the x-axis
    Then the box should be in the specific target with the position error threshold being less than or equal "0.35" cm in the y-axis
    Then the box should be in the specific target with the position error threshold being less than or equal "0.35" cm in the z-axis




