# Prompt

Design a REST API that will support querying for emergency incident records by the following:
1. The latest incident for a given phone number
2. All the incidents for a given phone number
3. All the incidents of the same emergency_type and/or status and/or phone number and/or time slice

When designing this system please discuss the following:
- Database technologies to support this type of data schema and required queries
- Performance considerations
- API interface
- Methods for verifying functionality and performance

You may use the following schema for the Emergency Incident records:
- phone_number (str) - Phone number of the device making the emergency call
- location (point) - The geodetic location of the emergency as an XY point
- emergency_type (str) - The type of emergency i.e. fire, burglary, car accident
- status (str) - The current status of the emergency incident i.e. responders dispatched, on scene
- created_time (int) - UNIX timestamp of when the incident record was created
