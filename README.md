### Four_Axis_Stage_Control

- Introduction\
  The four-axis stage enables movement along x,y,z axises and rotate along z-axis, which is comprised of two module, a gantry stage and a rotary stage.
  Can make use of either Windows-based PC or Ubuntu-based evaluation board, such as R-Pi or Jetson Nano, without accessibility of I/O pins.
  The controller of the gantry stage has integrated control signals from arms with respect to x,y,z direction, and can be communicated with USB port.
  The controller of the rotary stage is connected to Arduino, and can be communicated with USB port as well.

  This platform can be the base to do CNC, Laser cut, or measuring the properties.
  
- Hardware
  1. Jetson Orin Nano
  2. Gantry Stage (compatible to GRBL library, with controllers integrated)
  3. Rotary Stage (with Nema 17 stepper motor, without controller) 
  4. Controller for rotary stage
  5. Arduino Nano

- Communicate to Gantry
  GRBL library can make it easily to communicate with the controller when the COM port is well connected.
  To enhance the revolution and accuracy, the command must be able to specify the exact coordinate of the destination and the speed.
  Besides, in order to record the location, cartesian coordinates for x,y,z, it's necessary to receive information from controllers.

- Communicate to Rotary\
  - The rotary is equipped with Nema 17 stepper controller, from which there are four signals coming out, A+, A-, B+, B-.
  - A+, A- stands for one of two loops for the two phases motor and can be easily found by connecting any two wires together. If the motor can be rotated by hand, there's short circuit and could be either A+, A- pair or B+, B-. In most of the cases, the cables would be labeled. The four wires are then connected to a controller, which contains pins corresponding to A+, A-, B+, B-. That is, what the controller do is to energize the motor and convert the command to feed to the motor.
  - What we exactly do to actuate the motor is by communicating with the controller by send signals for pulses and directions. This is the reason that Arduino Nano is used here. We make use of the GPIO pin to generate nearly 5V to imply HIGH/LOW or CW/CCW.
  - In arduino program, set the GPIO pin to high then changed to low for one pulse.
  - Pulse/revolution can be found on the controller.
