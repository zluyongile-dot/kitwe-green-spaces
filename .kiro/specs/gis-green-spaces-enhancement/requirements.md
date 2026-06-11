# Requirements Document: GIS Green Spaces Enhancement

## Introduction

This document specifies the requirements for enhancing the Kitwe Green Spaces GIS web application. The enhancement adds a statistics section, a "Report a Green Space" form, and improved UI structure while preserving all existing map functionality. The system is a frontend-only HTML/CSS/JavaScript application using Leaflet.js for mapping, with data sourced from a canonical JavaScript dataset.

## Glossary

- **System**: The GIS Green Spaces web application frontend
- **Dataset**: The canonical GREEN_SPACES_DATA JavaScript object containing all green space records
- **Map**: The Leaflet.js interactive map component
- **Statistics_Section**: The UI component displaying aggregate data about green spaces
- **Report_Form**: The UI component allowing users to submit new green space suggestions
- **Filter**: The UI component allowing users to filter visible green spaces by type, ward, and area
- **GreenSpace**: A data record representing a single green space with properties including id, name, type, ward, area, and coordinates
- **Feature**: A GeoJSON Feature object wrapping a GreenSpace in the properties field
- **Marker**: A Leaflet map marker representing a green space location
- **Ward**: An administrative subdivision of Kitwe city

## Requirements

### Requirement 1: Canonical Dataset

**User Story:** As a developer, I want a single authoritative data source for all green spaces, so that the map, filters, and statistics always display consistent information.

#### Acceptance Criteria

1. THE System SHALL load green space data from a single global variable named GREEN_SPACES_DATA
2. THE Dataset SHALL be structured as a GeoJSON FeatureCollection with a features array
3. WHEN the Dataset is accessed, THE System SHALL provide exactly 51 green space records for Kitwe
4. THE Dataset SHALL include the following fields for each green space: id, name, type, ward, area_sq_m, latitude, longitude
5. THE Dataset SHALL support optional fields: description, facilities, accessibility
6. THE System SHALL use the Dataset as the source for map markers, filter operations, and statistics calculations

### Requirement 2: Data Validation

**User Story:** As a developer, I want all green space records to be validated, so that the application operates correctly with clean data.

#### Acceptance Criteria

1. FOR ALL GreenSpace records, THE id field SHALL be a unique integer
2. FOR ALL GreenSpace records, THE name field SHALL be a non-empty string
3. FOR ALL GreenSpace records, THE type field SHALL be one of: park, garden, forest, recreational, golf_course, public_square, sports_field, wetland
4. FOR ALL GreenSpace records, THE latitude field SHALL be in the range [-90, 90]
5. FOR ALL GreenSpace records, THE longitude field SHALL be in the range [-180, 180]
6. FOR ALL GreenSpace records, THE area_sq_m field SHALL be greater than or equal to 0

### Requirement 3: Map Initialisation and Display

**User Story:** As a user, I want to see an interactive map of Kitwe with all green spaces marked, so that I can explore their locations visually.

#### Acceptance Criteria

1. WHEN the page loads, THE System SHALL initialise a Leaflet map centred on Kitwe at coordinates [-12.8130, 28.2200] with zoom level 13
2. WHEN the Dataset is loaded, THE System SHALL render a marker for each green space at its latitude and longitude coordinates
3. THE System SHALL group markers by type into separate layer groups
4. THE System SHALL colour-code markers according to their type
5. WHEN a user clicks a marker, THE System SHALL display a popup showing the green space name, type, area, ward, and action buttons
6. THE Map SHALL use OpenStreetMap as the tile layer

### Requirement 4: Filter Functionality

**User Story:** As a user, I want to filter green spaces by type, ward, and minimum area, so that I can find spaces matching my specific criteria.

#### Acceptance Criteria

1. THE System SHALL provide a filter dropdown for green space type with options for all types plus an "all" option
2. THE System SHALL provide a filter dropdown for ward with options for all wards plus an "all" option
3. THE System SHALL provide a range slider for minimum area in square metres
4. WHEN a user applies filters, THE System SHALL display only markers that match all selected filter criteria
5. WHEN a user applies filters, THE Statistics_Section SHALL update to reflect only the filtered subset
6. WHEN a user clicks the reset button, THE System SHALL clear all filters and display all green spaces
7. THE Filter SHALL preserve existing map zoom and centre position when updating markers

### Requirement 5: Statistics Computation

**User Story:** As a user, I want to see aggregate statistics about green spaces, so that I can understand the overall distribution and coverage.

#### Acceptance Criteria

1. THE Statistics_Section SHALL display the total count of green spaces
2. THE Statistics_Section SHALL display the total area of all green spaces in hectares
3. THE Statistics_Section SHALL display the count of distinct wards containing green spaces
4. THE Statistics_Section SHALL display a breakdown of green space count by type
5. WHEN the Dataset changes or filters are applied, THE System SHALL recompute all statistics based on the current visible set
6. THE System SHALL convert area from square metres to hectares by dividing by 10000 and rounding to 1 decimal place
7. FOR ALL statistics computations, THE sum of counts by type SHALL equal the total count

### Requirement 6: Report Form Validation

**User Story:** As a user, I want to report a new green space with validation, so that I can contribute accurate information to the system.

#### Acceptance Criteria

1. THE Report_Form SHALL require the following fields: reporter name, space name, space type, ward, description
2. WHEN a user submits the form with any required field empty, THE System SHALL display an error message for each missing field
3. WHEN a user submits the form with a description shorter than 10 characters, THE System SHALL display an error message
4. WHEN a user submits the form with all valid fields, THE System SHALL accept the submission
5. THE Report_Form SHALL provide a dropdown for space type containing all valid green space types
6. THE System SHALL validate all fields before processing the submission
7. WHEN validation fails, THE System SHALL not clear the form fields

### Requirement 7: Report Form Submission

**User Story:** As a user, I want to submit a green space report and receive confirmation, so that I know my contribution was recorded.

#### Acceptance Criteria

1. WHEN a user submits a valid report, THE System SHALL store the report in browser localStorage
2. WHEN a user submits a valid report, THE System SHALL add a timestamp field with the current ISO 8601 date and time
3. WHEN a user submits a valid report, THE System SHALL display a confirmation message containing the submitted space name
4. WHEN a user submits a valid report, THE System SHALL clear all form fields after successful submission
5. THE confirmation message SHALL automatically hide after 5 seconds
6. WHERE a backend API is available, THE System SHALL attempt to POST the report to /api/add-green-space
7. IF the backend API call fails, THE System SHALL still store the report locally and show the confirmation message

### Requirement 8: UI Structure and Layout

**User Story:** As a user, I want a clearly organised sidebar with labelled sections, so that I can easily find and use different features.

#### Acceptance Criteria

1. THE System SHALL organise the sidebar into four distinct sections: Map Controls, Filter, Statistics, and Report a Green Space
2. THE System SHALL label each section with an icon and descriptive heading
3. THE Map Controls section SHALL contain the logo, title, search input, and Find Parks Near Me button
4. THE Filter section SHALL contain type dropdown, ward dropdown, area slider, and apply/reset buttons
5. THE Statistics section SHALL contain total count, total area, ward count, and type breakdown displays
6. THE Report_Form section SHALL contain all report input fields, submit button, and confirmation message area
7. THE System SHALL make each section visually distinct and easy to identify

### Requirement 9: Error Handling and Fallback

**User Story:** As a user, I want the application to handle errors gracefully, so that I can continue using available features even when problems occur.

#### Acceptance Criteria

1. IF the Dataset fails to load, THE System SHALL check for a fallback dataset named FALLBACK_GREEN_SPACES
2. IF the Dataset fails to load, THE System SHALL display a notification informing the user that fallback data is being used
3. WHEN updating statistics, IF a required DOM element is missing, THE System SHALL skip that element without throwing an error
4. WHEN submitting a report, IF the backend API is unavailable, THE System SHALL continue with local storage only
5. THE System SHALL guard all DOM updates with null checks to prevent runtime errors
6. WHEN any error occurs, THE System SHALL log the error to the console for debugging

### Requirement 10: Performance Requirements

**User Story:** As a user, I want the application to respond quickly to my interactions, so that I have a smooth experience.

#### Acceptance Criteria

1. WHEN computing statistics for the full dataset, THE System SHALL complete the calculation in less than 10 milliseconds
2. WHEN applying filters, THE System SHALL update both the map and statistics within 100 milliseconds
3. WHEN the page loads, THE System SHALL render all 51 markers within 500 milliseconds
4. THE System SHALL recompute statistics synchronously on each filter change without noticeable delay
5. THE System SHALL clear and re-render all markers when filters change without pagination

### Requirement 11: Data Persistence

**User Story:** As a user, I want my submitted reports to be saved, so that they are not lost if I close the browser.

#### Acceptance Criteria

1. WHEN a report is submitted, THE System SHALL retrieve existing reports from localStorage under the key "greenSpaceReports"
2. WHEN a report is submitted, THE System SHALL append the new report to the existing reports array
3. WHEN a report is submitted, THE System SHALL save the updated reports array back to localStorage as a JSON string
4. IF no existing reports are found in localStorage, THE System SHALL initialise an empty array
5. THE System SHALL parse the localStorage JSON string safely and handle parse errors

### Requirement 12: Security and Input Sanitisation

**User Story:** As a developer, I want user inputs to be handled safely, so that the application is protected from malicious content.

#### Acceptance Criteria

1. WHEN displaying user-submitted description text, THE System SHALL HTML-escape the content to prevent XSS attacks
2. THE System SHALL trim whitespace from all text inputs before validation
3. WHERE the backend API is enabled, THE server SHALL sanitise all inputs before database insertion
4. THE Report_Form SHALL not expose any authentication endpoints or sensitive operations
5. THE System SHALL treat all user inputs as untrusted data
