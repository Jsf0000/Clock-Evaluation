# Clock Program Documentation

This documentation provides an overview of how to run and debug the Clock Program, including instructions for operating the main clock function and the message customization feature.

## Running the Program

### Starting the Main Clock

To initiate the main clock functionality, use the following command:

```commandline
python ClockController.py
```

#### Example of Running the Main Clock

Executing the command above will start the clock, producing output similar to:

```commandline
python ClockController.py
2024-03-10 18:16:39- INFO - tick  
2024-03-10 18:16:40- INFO - tick  
2024-03-10 18:16:41- INFO - tick  
2024-03-10 18:16:42- INFO - tick  
2024-03-10 18:16:43- INFO - tick  
```

### Customizing Messages

The program allows customization of messages for seconds, minutes, and hours through the `ChangeMessagesController.py` script. There are three options available:

1. `--second_message`: Customize the message displayed every second.
2. `--minute_message`: Customize the message displayed every minute.
3. `--hour_message`: Customize the message displayed every hour.

#### Commands for Changing Messages

To change these messages, use the following commands:

```commandline
python ChangeMessagesController.py --second_message second
python ChangeMessagesController.py --minute_message minute
python ChangeMessagesController.py --hour_message hour
```

#### Example of Changing Messages

```commandline
python ChangeMessagesController.py --second_message second
2024-03-09 20:08:12- INFO - Message changed -- New messages  
2024-03-09 20:08:12- INFO - {
    "second_message": "second",
    "minute_message": "tock",
    "hour_message": "bong"
}  
```

## Important Considerations

- The program's files are located at `/Clock-Evaluation/controller`.
- Changes made using `ChangeMessagesController.py` are reflected after 10 minutes while `ClockController.py` is running.
- `ClockController.py` runs for a duration of 3 hours, which can be adjusted in the settings file.
- Both `ClockController.py` and `ChangeMessagesController.py` can run simultaneously in separate terminals.

## Debugging the Program

Unit tests for the program are located in the `/Clock-Evaluation/testing` directory.

### Running Unit Tests

To run all unit tests, execute:

```commandline
python -m unittest discover
```

#### Example Output of Unit Tests

```commandline
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

### Unit Test Files

There are two primary unit test files:

1. `testChangedMessage`: Tests message customization functionality.
2. `testClock`: Contains three tests focusing on message display correctness, changes in message display, and the program's termination after exceeding a 3-hour limit.

## Additional Information

### Logger System

- All output messages include a timestamp, utilizing a logging system.
- Logs are saved in the `/Clock-Evaluation/Logs` directory.

### Program Structure

- **Controller**: Contains scripts to run the clock and change messages.
- **Logs**: Directory for storing logs.
- **Services**: Contains the logic for the clock and message change system.
- **Settings**: Includes configuration files, such as time limits, log paths, and JSON files for message changes.
- **Utils**: Houses constants, logging logic, and auxiliary methods (e.g., JSON read/write functions).
