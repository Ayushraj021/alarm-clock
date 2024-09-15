# Python GUI Alarm Clock

A graphical user interface (GUI) based **Alarm Clock** application built with Python using `Tkinter` for the interface and `pygame` for sound alerts. The alarm clock allows users to set a specific time, at which the alarm will trigger an alert sound.

## Features

- **Set Alarm Time**: Users can set the alarm using hour, minute, and second selection along with AM/PM options.
- **Alarm Activation**: The user can activate or deactivate the alarm using radio buttons.
- **Sound Alert**: The alarm plays a sound (loaded from a `.wav` file) when the time is reached.
- **Customizable**: Easy to modify the alarm sound or adjust the interface as needed.

## Technologies Used

- **Python**: Programming language used for the logic.
- **Tkinter**: Standard Python library for creating the graphical user interface (GUI).
- **Pygame**: Used to play audio when the alarm goes off.
- **Pillow (PIL)**: Used to handle image manipulation in the GUI.

## Prerequisites

Before running the application, ensure you have the following Python libraries installed:

```bash
pip install tkinter
pip install pygame
pip install pillow
```

If you don't have the `Tkinter` library installed, install it as follows for Linux users:

```bash
sudo apt-get install python3-tk
```

## Setup and Running the Alarm Clock

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/alarm-clock-python.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd alarm-clock-python
    ```

3. **Ensure the Required Files Are Present**:
    - `alarm_clock.py`: The main Python script to run the alarm.
    - `music.wav`: The sound file that plays when the alarm triggers.
    - `image.png`: The image to display in the GUI.
    
4. **Run the Alarm Clock**:
    ```bash
    python alarm_clock.py
    ```

## How to Use

1. Launch the application.
2. Set the alarm time by selecting **hours**, **minutes**, **seconds**, and **AM/PM**.
3. Click the **Activate** button to enable the alarm.
4. When the set time is reached, an alarm sound will play, and a message will be printed to the console.
5. To stop the alarm, click the **Deactivate** button.

## Customization

- **Alarm Sound**: You can replace `music.wav` with any `.wav` file of your choice for a custom alarm sound.
- **Image**: Update `image.png` in the project directory to change the logo or image displayed in the GUI.

## Screenshots

*(Optional: Add some screenshots of your GUI to give users a preview.)*

## License

This project is open-source and available under the [MIT License](LICENSE).
