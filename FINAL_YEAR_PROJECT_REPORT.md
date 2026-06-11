# MULUNGUSHI UNIVERSITY

## SCHOOL OF SCIENCE, ENGINEERING AND TECHNOLOGY (SSET)

### DEPARTMENT OF COMPUTER SCIENCE AND IT

---

# PROJECT REPORT TITLE: 
## GIS-BASED WEB APPLICATION FOR URBAN GREEN SPACE MAPPING IN KITWE

---

**NAME:** MUKENDWA LUYONGILE  
**STUDENT ID:** 202201912  
**COURSE:** ICT432 CAPSTONE PROJECT REPORT  
**PROGRAMME:** BACHELOR OF SCIENCE IN COMPUTER SCIENCE  
**SUPERVISOR:** MR. NYIRENDA

---

**THIS REPORT IS SUBMITTED IN PARTIAL FULFILMENT FOR THE AWARD OF BACHELOR OF COMPUTER SCIENCE FOR THE 2024/2025 ACADEMIC YEAR**

---

*Date: [Submission Date]*

---

## TABLE OF CONTENTS

- [DECLARATION](#declaration)
- [ACKNOWLEDGEMENT](#acknowledgement)
- [ABSTRACT](#abstract)
- [LIST OF FIGURES](#list-of-figures)
- [LIST OF TABLES](#list-of-tables)
- [ACRONYMS AND ABBREVIATIONS](#acronyms-and-abbreviations)
- [CHAPTER 1: INTRODUCTION](#chapter-1-introduction)
  - 1.1 Introduction
  - 1.2 Problem Statement
  - 1.3 Aim
  - 1.4 Objectives
  - 1.5 Project Scope
  - 1.6 Project Justification
  - 1.7 Summary / Conclusion
- [CHAPTER 2: LITERATURE REVIEW](#chapter-2-literature-review)
  - 2.1 Introduction
  - 2.2 Related Literature
  - 2.3 Review of Existing/Current Systems
  - 2.4 Comparison of Reviewed Systems
  - 2.5 Proposed System
  - 2.6 Summary / Conclusion
- [CHAPTER 3: RESEARCH METHODOLOGY](#chapter-3-research-methodology)
  - 3.1 Introduction
  - 3.2 Selected Methodology (Agile Model)
  - 3.3 Justification of the Agile Software Development Model
  - 3.4 Technologies and Frameworks Used
  - 3.5 Data Collection and Analysis
  - 3.6 Ethical Considerations
  - 3.7 Summary / Conclusion
- [CHAPTER 4: SYSTEM ANALYSIS AND DESIGN](#chapter-4-system-analysis-and-design)
  - 4.1 Introduction
  - 4.2 System Analysis
  - 4.3 System Design
  - 4.4 Summary/Conclusion
- [CHAPTER 5: SYSTEM IMPLEMENTATION](#chapter-5-system-implementation)
  - 5.1 Introduction
  - 5.2 Development Environment
  - 5.3 Database Implementation
  - 5.4 Backend Implementation
  - 5.5 Frontend Implementation
  - 5.6 GIS Integration
  - 5.7 Summary/Conclusion
- [CHAPTER 6: RESULT ANALYSIS AND TESTING](#chapter-6-result-analysis-and-testing)
  - 6.1 Introduction
  - 6.2 Environment Description
  - 6.3 Unit Testing
  - 6.4 System Testing
  - 6.5 Test Scenarios
  - 6.6 Summary/Conclusion
- [CHAPTER 7: PROJECT MANAGEMENT](#chapter-7-project-management)
  - 7.1 Introduction
  - 7.2 Risk and Quality Management
  - 7.3 Risk Analysis/Risk Register
  - 7.4 Effort Costing Model
  - 7.5 Budget
  - 7.6 Scheduling and Work Plan
  - 7.7 Summary / Conclusion
- [CHAPTER 8: CRITICAL EVALUATION](#chapter-8-critical-evaluation)
  - 8.1 Introduction
  - 8.2 Reason for Undertaking the Project
  - 8.3 Main Learning Outcomes
  - 8.4 Challenges Encountered
  - 8.5 Future Work
  - 8.6 Conclusion
- [CHAPTER 9: CONCLUSION](#chapter-9-conclusion)
  - 9.1 Introduction
  - 9.2 Research Contribution
  - 9.3 Final Remarks
- [REFERENCES](#references)

---

## DECLARATION

I confirm that this project report is my original work and has not been submitted for a degree at any other university. I declare that the project report titled **"GIS-Based Web Application for Urban Green Space Mapping in Kitwe"** submitted for the course **"ICT 432"** is entirely my own work and has not been used as the basis for awarding any degree, associateship, fellowship, or any similar qualification. I understand that failing to credit sources appropriately may be regarded as plagiarism.

This research project has been submitted for review with the approval of my University Supervisor.

**Author:** Mukendwa Luyongile  
**Date:** _______________  
**Signature:** ____________________

**Supervisor:** Mr. Nyirenda  
**Date:** _______________  
**Signature:** ____________________

---

## ACKNOWLEDGEMENT

I would like to express my heartfelt gratitude to my supervisor, **Mr. Nyirenda**, for his invaluable support, insightful guidance, and continuous encouragement throughout the development of this project. His constructive feedback and expertise have been crucial to my progress and the successful completion of this report.

I extend my deepest thanks to the **Kitwe City Council** and the **Zambia Environmental Management Agency (ZEMA)** for their cooperation during the requirement-gathering phase and for providing valuable insights into urban environmental management challenges.

I am also grateful to the faculty members of **Mulungushi University**, particularly the Department of Computer Science and IT, for imparting knowledge and providing a strong academic foundation throughout my studies. Their dedication and teaching have equipped me with the skills necessary to undertake this project.

I owe a debt of gratitude to my **father and friends** for their unconditional support, understanding, and motivation during the challenging periods of this academic journey. Their belief in me has been my greatest strength.

Above all, I am thankful to **God** for granting me the wisdom, perseverance, and resilience to reach this milestone. It is through His grace that I have come this far.

---

## ABSTRACT

The rapid urbanization of Kitwe, Zambia, has placed significant pressure on its urban green spaces (UGS), leading to their fragmentation and loss. This degradation is exacerbated by the lack of a centralized, digital system for mapping and monitoring these vital environmental assets. This project aimed to address this gap by designing and developing a **GIS-based web application** for the interactive mapping and participatory management of UGS in Kitwe.

The system was developed using an **Agile methodology**, leveraging a stack of open-source technologies including a **PostgreSQL/PostGIS** spatial database for data management, a **Python Flask** framework for the backend API, and the **Leaflet.js** library for interactive frontend map visualization. The application integrates spatial data from multiple sources including OpenStreetMap, GPS field surveys, and satellite imagery to create a comprehensive digital repository of Kitwe's green spaces.

The resulting web application provides functionalities for visualizing the spatial distribution of green spaces, filtering them by attributes such as type, size, and ward location, and includes a **public feedback module** to facilitate citizen reporting of new or degraded green spaces. An administrative dashboard enables authorized users from the Kitwe City Council and ZEMA to update spatial data, manage user submissions, and generate analytical reports.

The system was tested using a combination of unit testing, integration testing, and user acceptance testing with stakeholders. Results demonstrate that the application successfully addresses the identified problem by providing an accessible, interactive platform for green space management. The project contributes to sustainable urban development goals by empowering decision-makers with accurate geospatial information and promoting public participation in environmental conservation.

**Keywords:** Geographic Information System (GIS), Web Application, Urban Green Spaces, Kitwe, Sustainable Development, Open Source, PostGIS, Leaflet.js, Flask, Spatial Database, Environmental Management, Participatory Mapping.

---

## LIST OF FIGURES

- Figure 1: Urban Green Space Distribution in Kitwe
- Figure 2: Benefits of Urban Green Spaces
- Figure 3: Comparison Table of Reviewed Systems
- Figure 4: Phases of Agile Methodology
- Figure 5: Use Case Diagram for the GIS Web Application
- Figure 6: Level 1 Data Flow Diagram
- Figure 7: System Architecture Diagram
- Figure 8: Database Entity-Relationship Diagram
- Figure 9: Admin Dashboard Sequence Diagram
- Figure 10: Public Feedback Submission Sequence
- Figure 11: Main Map Interface Screenshot
- Figure 12: Green Space Details View
- Figure 13: Admin Dashboard Interface
- Figure 14: Feedback Submission Form
- Figure 15: Filter and Search Functionality
- Figure 16: Spatial Analysis Results
- Figure 17: Mobile Responsive View
- Figure 18: Database Schema Implementation
- Figure 19: API Endpoint Testing Results
- Figure 20: System Performance Metrics
- Figure 21: User Acceptance Testing Results
- Figure 22: Risk Register Matrix
- Figure 23: COCOMO II Effort Estimation
- Figure 24: Project Timeline Gantt Chart
- Figure 25: Budget Breakdown Chart

---

## LIST OF TABLES

- Table 1: Comparison of Existing GIS Systems
- Table 2: Functional Requirements
- Table 3: Non-Functional Requirements
- Table 4: Technology Stack Summary
- Table 5: Database Tables and Attributes
- Table 6: API Endpoints Documentation
- Table 7: Unit Test Cases
- Table 8: Integration Test Results
- Table 9: User Acceptance Test Scenarios
- Table 10: Risk Register
- Table 11: Effort Estimation by Phase
- Table 12: Budget Breakdown
- Table 13: Project Schedule
- Table 14: System Performance Benchmarks

---

## ACRONYMS AND ABBREVIATIONS

| Acronym/Abbreviation | Full Meaning |
|----------------------|--------------|
| GIS | Geographic Information System |
| UGS | Urban Green Spaces |
| API | Application Programming Interface |
| ZEMA | Zambia Environmental Management Agency |
| OSM | OpenStreetMap |
| QGIS | Quantum Geographic Information System |
| SQL | Structured Query Language |
| REST | Representational State Transfer |
| JSON | JavaScript Object Notation |
| HTML | HyperText Markup Language |
| CSS | Cascading Style Sheets |
| HTTP | HyperText Transfer Protocol |
| HTTPS | HyperText Transfer Protocol Secure |
| GPS | Global Positioning System |
| CRUD | Create, Read, Update, Delete |
| UI | User Interface |
| UX | User Experience |
| SDG | Sustainable Development Goals |
| COCOMO | Constructive Cost Model |
| UAT | User Acceptance Testing |
| IDE | Integrated Development Environment |

---



## CHAPTER 1: INTRODUCTION

### 1.1 Introduction

Urban green spaces are areas within cities that are partly or completely covered with vegetation and accessible to the public. These spaces include public parks, community gardens, forests, sports fields, cemeteries, and natural reserves. They provide vital environmental, social, and health benefits to city residents by reducing air pollution, mitigating urban heat, supporting biodiversity, and offering recreational areas that improve quality of life (Kabisch et al., 2017).

In Zambia, rapid urbanization has placed significant pressure on green spaces, especially in cities like Kitwe, which is one of the most industrialized areas in the Copperbelt Province. Uncontrolled expansion of housing, infrastructure, and mining activities has led to the fragmentation and loss of green areas that were once abundant within the city. This has resulted in reduced ecosystem services, poor air quality, and limited recreational opportunities for residents (Ministry of Green Economy and Environment, 2022).

The need for a data-driven solution that enables the identification, mapping, and monitoring of urban green spaces has therefore become increasingly urgent. Geographic Information Systems (GIS) provide an effective platform for spatial data visualization, environmental monitoring, and decision-making (Goodchild, 2018). By developing a GIS-based web application, stakeholders such as municipal authorities, environmental organizations, and citizens can have access to real-time information on the distribution and condition of green spaces.

This project aims to design and implement a GIS-enabled mapping system that will visualize, analyze, and support the management of green spaces in Kitwe. It integrates open-source geospatial tools with publicly available datasets to generate interactive maps, allowing users to explore existing green areas, report issues, and recommend new sites for preservation or rehabilitation. The system addresses the critical gap in digital environmental management tools available to Zambian cities, contributing to sustainable urban development and environmental conservation efforts.

### 1.2 Problem Statement

Urban green spaces are increasingly under threat in Kitwe due to urban sprawl, industrial development, poor land management practices, and lack of coordinated environmental planning. Many green areas are either encroached upon or degraded because there is no centralized digital system for mapping, monitoring, and managing them (Amoako & Korah, 2016).

Currently, city authorities and environmental planners rely on outdated paper-based maps or incomplete datasets, making it difficult to assess the real extent and condition of green spaces. This absence of up-to-date spatial data has hindered efforts to enforce sustainable land use and promote community participation in environmental management. The Kitwe City Council and ZEMA lack an integrated platform that provides accurate, accessible, and interactive information about the city's green infrastructure.

Without a proper digital mapping system, it becomes nearly impossible to make data-informed decisions on urban planning, tree planting, environmental protection, and sustainable land use. The fragmentation of environmental data across different departments and the lack of public access to this information further compound the problem. Citizens have no mechanism to report degraded green spaces or suggest new areas for conservation, limiting community engagement in environmental stewardship.

Furthermore, the absence of spatial analysis capabilities prevents planners from understanding patterns of green space distribution, identifying underserved areas, or assessing the impact of urban development on environmental assets. This gap in technological infrastructure directly impacts the city's ability to meet national environmental goals and international commitments such as the UN Sustainable Development Goals (SDGs), particularly SDG 11 (Sustainable Cities and Communities) and SDG 15 (Life on Land).

Therefore, there is an urgent need for a GIS-based web system that provides accurate, interactive, and easily accessible information on Kitwe's green spaces, enabling evidence-based decision-making and fostering public participation in environmental conservation.

### 1.3 Aim

To develop a GIS-based web application for mapping, analyzing, and managing urban green spaces in Kitwe to support sustainable environmental planning and promote community engagement in green space conservation.

### 1.4 Objectives

The specific objectives of this project are to:

1. **Identify and collect** spatial data on existing urban green spaces in Kitwe from multiple sources including OpenStreetMap, GPS surveys, and satellite imagery.

2. **Design and develop** a GIS-based web system that visualizes and manages spatial data on green spaces using open-source technologies.

3. **Integrate** interactive mapping technologies (Leaflet.js and OpenStreetMap) for dynamic visualization and user interaction.

4. **Implement** search, filter, and analysis functionalities that enable users to explore green space data based on criteria such as size, location, type, and ward.

5. **Develop** a public feedback module that allows citizens to submit information about new or degraded green spaces, promoting participatory environmental management.

6. **Create** an administrative dashboard for authorized users to manage spatial data, review submissions, and generate analytical reports.

7. **Support** municipal decision-making by providing spatial statistics, distribution analysis, and reporting tools for environmental planning.

8. **Evaluate** the system's effectiveness through comprehensive testing including unit tests, integration tests, and user acceptance testing with stakeholders.

### 1.5 Project Scope

The project focuses primarily on the urban area of Kitwe in the Copperbelt Province of Zambia. The proposed system targets public and semi-public green spaces such as parks, gardens, forest patches, sports fields, and open recreational areas.

**The main functionalities include:**

- **Spatial Data Management:** Collection, storage, and management of green space data using PostgreSQL/PostGIS spatial database
- **Interactive Map Visualization:** Web-based interface displaying green spaces on an interactive map with zoom, pan, and layer control features
- **Data Input and Updates:** Administrative dashboard for authorized users to add, edit, and delete green space records
- **Search and Filter:** Tools enabling users to search for specific green spaces and filter by attributes such as type, size, and location
- **Spatial Analysis:** Basic analytical tools for calculating total green space area, distribution by ward, and accessibility metrics
- **Public Feedback Module:** Form allowing citizens to report new green spaces or issues with existing ones
- **Reporting:** Generation of summary reports and statistics for decision-making purposes
- **User Authentication:** Secure login system for administrative users

**Limitations:**

The system will not cover:
- Private gardens or inaccessible land due to data availability and privacy constraints
- Advanced predictive modeling or machine learning-based analysis
- Real-time satellite imagery processing
- Mobile application development (web-responsive design only)
- Integration with external government databases (simulated through mock data)

The project emphasizes data visualization, basic spatial analysis, and user interaction rather than complex environmental modeling. The focus is on creating a functional prototype that demonstrates the feasibility and value of GIS technology for urban environmental management in the Zambian context.

### 1.6 Project Justification

This project is motivated by the increasing need for data-driven environmental management and sustainable urban planning in Zambia. Kitwe's urban growth has led to the loss of natural landscapes, making it crucial to protect and restore remaining green areas (Ministry of Green Economy and Environment, 2022).

**The GIS-based web application will:**

1. **Provide a Centralized Digital Repository:** Consolidate fragmented green space data into a single, accessible platform, eliminating reliance on outdated paper maps and disconnected datasets.

2. **Support Evidence-Based Decision Making:** Enable the Kitwe City Council and ZEMA to make informed decisions about land use planning, environmental protection, and resource allocation based on accurate spatial data and analysis.

3. **Promote Transparency and Accountability:** Make environmental data publicly accessible, fostering transparency in government operations and enabling citizens to hold authorities accountable for green space management.

4. **Encourage Citizen Engagement:** Provide a mechanism for public participation in environmental stewardship through the feedback module, empowering residents to contribute to conservation efforts.

5. **Facilitate Collaboration:** Create a platform for collaboration between stakeholders including government agencies, environmental NGOs, researchers, and community organizations.

6. **Contribute to National and International Goals:** Support Zambia's Vision 2030 for sustainable development and contribute to achieving UN Sustainable Development Goals, particularly SDG 11 (Sustainable Cities and Communities) and SDG 15 (Life on Land).

7. **Demonstrate Technological Innovation:** Showcase how open-source geospatial technologies can be applied cost-effectively to address local environmental challenges, providing a model that can be replicated in other Zambian cities.

8. **Build Technical Capacity:** Contribute to the growing body of knowledge on GIS applications in Zambia and provide a practical learning resource for students and professionals interested in geospatial technology.

**Academic and Professional Significance:**

From an academic perspective, this project demonstrates the practical application of computer science principles, software engineering methodologies, and geospatial technologies to solve real-world problems. It aligns with Mulungushi University's commitment to fostering innovative ICT solutions that promote national development.

Professionally, the project addresses a genuine need identified by local authorities and environmental agencies, ensuring that the research has immediate practical relevance and potential for real-world deployment. The use of open-source technologies ensures sustainability and reduces dependency on expensive proprietary software, making the solution accessible to resource-constrained government agencies.

### 1.7 Summary / Conclusion

This chapter has presented the background, problem statement, aim, objectives, scope, and justification for developing a GIS-based system to map urban green spaces in Kitwe. The chapter establishes the importance of using modern geospatial technologies for addressing environmental management challenges in rapidly urbanizing cities.

The proposed solution—an interactive GIS web application—will provide city authorities and the general public with an accessible tool for green space monitoring, planning, and decision-making. By addressing the identified gap in digital environmental management infrastructure, the project contributes to sustainable urban development and environmental conservation efforts in Zambia.

The subsequent chapters will explore the theoretical foundations through a literature review, detail the research methodology and technologies employed, present the system analysis and design, document the implementation process, analyze testing results, discuss project management aspects, and provide a critical evaluation of the work undertaken.

---



## CHAPTER 2: LITERATURE REVIEW

### 2.1 Introduction

This chapter reviews relevant literature to explore how Geographic Information Systems (GIS) and web technologies can address the limitations of traditional urban green space management. We examine existing GIS-based environmental systems, compare these systems with conventional methods, and analyze both the benefits and challenges of implementing web-GIS solutions in the context of developing countries.

The literature review is structured to provide a comprehensive understanding of: (1) the definition and importance of urban green spaces, (2) the role of GIS in urban environmental management, (3) web-based GIS systems and their applications, (4) existing systems for green space mapping globally and in Africa, and (5) gaps in current approaches that justify the development of the proposed system.

This review lays the foundation for understanding the need for a decentralized, accessible, and user-friendly green space mapping system tailored to the specific context of Kitwe, Zambia.

### 2.2 Related Literature

#### 2.2.1 Definition and Importance of Urban Green Spaces

Urban green spaces (UGS) are defined as areas of vegetation in urban environments that provide ecological, social, and economic benefits to communities (Kabisch et al., 2017). They are integral to environmental sustainability as they enhance air quality, mitigate the urban heat island effect, and support biodiversity (WHO, 2016). Furthermore, green spaces contribute to physical and mental health, offering recreational and social interaction areas (Wolch et al., 2014).

Research by Taylor and Hochuli (2017) demonstrates that urban green spaces play a critical role in climate change adaptation by reducing surface temperatures and managing stormwater runoff. In the African context, Cilliers et al. (2013) found that green spaces in South African cities provide essential ecosystem services but are often undervalued in urban planning processes.

In Zambia, the Ministry of Green Economy and Environment (2022) highlights that urbanization has reduced natural vegetation cover, necessitating innovative digital approaches to monitor environmental change. Urban centers like Kitwe, Lusaka, and Ndola face rapid population growth that often results in encroachment on public green spaces. The lack of systematic documentation and monitoring of these spaces has led to their gradual disappearance, with significant implications for urban environmental quality and public health.

#### 2.2.2 GIS in Urban Environmental Management

Geographic Information Systems (GIS) play a crucial role in capturing, storing, analyzing, and visualizing spatial data for environmental management. GIS enables integration of multiple datasets to support spatial decision-making in urban planning (Goodchild, 2018). According to UN-Habitat (2020), GIS has been instrumental in promoting sustainable cities through land-use planning and green infrastructure monitoring.

Longley et al. (2015) describe GIS as a framework for gathering, managing, and analyzing spatial and geographic data, emphasizing its power to reveal patterns, relationships, and trends that are not apparent in traditional tabular data. In the context of urban green spaces, GIS provides tools for:

- **Spatial Inventory:** Documenting the location, extent, and characteristics of green spaces
- **Accessibility Analysis:** Assessing how easily residents can reach green spaces
- **Change Detection:** Monitoring the loss or gain of green areas over time
- **Planning Support:** Identifying optimal locations for new green spaces based on population distribution and existing coverage

A study by Onyeka and Igbokwe (2019) in Nigeria demonstrated how GIS mapping improved the understanding of green space distribution in Enugu, revealing significant disparities in access across different neighborhoods. Similarly, Amoako and Korah (2016) used GIS tools to assess accessibility to green spaces in Accra, Ghana, finding that low-income areas had significantly less access to quality green spaces compared to affluent neighborhoods.

These studies show that GIS can effectively identify and manage urban environmental resources, providing evidence for policy interventions and resource allocation decisions.

#### 2.2.3 Web-Based GIS Systems

The evolution of web technologies has transformed GIS from desktop-based systems to web-based interactive applications, improving accessibility and collaboration. Web GIS integrates spatial databases, mapping APIs, and visualization tools accessible through web browsers (Fu and Sun, 2011).

Peng and Tsou (2003) identify several advantages of web-based GIS over traditional desktop GIS:

- **Accessibility:** Users can access spatial data from anywhere with an internet connection
- **Cost-Effectiveness:** Eliminates the need for expensive desktop GIS software licenses
- **Collaboration:** Multiple users can view and interact with the same data simultaneously
- **Real-Time Updates:** Data can be updated centrally and immediately reflected for all users
- **User-Friendly Interfaces:** Web interfaces can be designed for non-technical users

For example, OpenStreetMap and Google Maps API have enabled open-source development of customized environmental monitoring platforms. Tian et al. (2020) developed a web-based GIS system for urban forest management in China, which allowed real-time monitoring and data sharing among stakeholders. Their system demonstrated improved coordination between forestry departments and increased public awareness of urban forest resources.

In Africa, Makange et al. (2022) proposed a web GIS for managing green spaces in Dar es Salaam, Tanzania. Their system demonstrated the potential for community participation in environmental mapping through mobile data collection tools and online visualization. However, they noted challenges related to internet connectivity and the need for capacity building among local government staff.

#### 2.2.4 Participatory GIS and Citizen Science

Recent trends in GIS emphasize participatory approaches that engage citizens in data collection and environmental monitoring. Participatory GIS (PGIS) empowers communities to contribute local knowledge and observations, enriching official datasets and promoting environmental stewardship (Sieber, 2006).

Brown and Kyttä (2014) discuss the concept of "Public Participation GIS" (PPGIS), which uses web-based mapping tools to gather spatial information from the public. Their research shows that PPGIS can reveal community values and preferences that might be overlooked in traditional planning processes.

In the context of urban green spaces, citizen science initiatives have successfully engaged residents in monitoring park conditions, reporting maintenance issues, and suggesting improvements. Haklay (2013) describes how platforms like "Fix My Street" in the UK have enabled citizens to report local environmental issues, creating a feedback loop between residents and local authorities.

### 2.3 Review of Existing/Current Systems

In the environmental management sector, various systems have been developed to address the challenges of mapping and monitoring urban green spaces. This section examines some widely used and relevant systems, their capabilities, and limitations that justify exploring alternative solutions tailored to the Zambian context.

#### (a) Global Forest Watch (GFW)

Global Forest Watch is an international platform developed by the World Resources Institute that uses satellite data and GIS to monitor global forest cover changes in near real-time (Hansen et al., 2013). The system provides:

- High-resolution satellite imagery analysis
- Deforestation alerts and monitoring
- Data visualization and download capabilities
- Integration with multiple data sources

**Strengths:**
- Comprehensive global coverage
- Regular updates using satellite data
- Open access to data and tools
- Strong analytical capabilities

**Limitations:**
- Focused on forests rather than urban green spaces
- Not localized for specific cities like Kitwe
- Requires technical expertise to interpret data
- Limited functionality for community engagement

#### (b) Zambia Environmental Information Management System (ZEIMS)

Managed by ZEMA, ZEIMS collects environmental data across Zambia including information on protected areas, pollution monitoring, and environmental impact assessments (ZEMA, 2022).

**Strengths:**
- National coverage of Zambia
- Official government system
- Comprehensive environmental data

**Limitations:**
- Lacks an interactive web-mapping interface for citizens
- No city-specific green space visualization
- Restricted access (not publicly available)
- Outdated user interface
- Limited spatial analysis capabilities

#### (c) GreenSpaces Map – Open Data (UK)

An online map developed by Ordnance Survey (UK) that displays public parks, gardens, and reserves. The system provides detailed information about green space types, sizes, and accessibility (Ordnance Survey, 2020).

**Strengths:**
- Highly functional and user-friendly interface
- Comprehensive data coverage
- Regular updates
- Integration with other government datasets

**Limitations:**
- Depends on advanced data infrastructure not available in Zambia
- Context-specific to UK planning regulations
- Requires significant resources for maintenance
- Not adaptable to developing country contexts

#### (d) Lusaka Urban Greening Project

Implemented by UN-Habitat (2021) in collaboration with the Zambian Ministry of Local Government, this project focuses on increasing tree cover and monitoring urban green networks in Lusaka.

**Strengths:**
- Locally relevant to Zambian context
- Focus on urban greening initiatives
- Collaboration with government agencies

**Limitations:**
- Lacks an integrated public GIS dashboard for visualization
- Limited to Lusaka (not available for Kitwe)
- No interactive mapping component
- Minimal citizen engagement features

#### (e) iTree Platform

Developed by the US Forest Service, iTree is a suite of tools for assessing and managing urban forests. It provides ecosystem service valuations and environmental benefit calculations (USDA Forest Service, 2020).

**Strengths:**
- Sophisticated environmental modeling
- Quantifies ecosystem services
- Scientific credibility

**Limitations:**
- Primarily designed for North American tree species
- Requires extensive field data collection
- Complex for non-technical users
- Not web-based for public access

These systems show the progress made globally and regionally in green space mapping. However, there is a noticeable gap in localized, city-specific, and citizen-accessible GIS systems for Zambian urban areas such as Kitwe.

### 2.4 Comparison of Reviewed Systems

The following table provides a comprehensive comparison of the reviewed systems, highlighting their key features and limitations in relation to the requirements for a Kitwe-specific green space mapping system:

**Table 1: Comparison of Existing GIS Systems**

| System | Geographic Coverage | Public Accessibility | Interactivity | Data Update Frequency | Citizen Participation | Limitations |
|--------|-------------------|---------------------|---------------|---------------------|---------------------|-------------|
| Global Forest Watch | Global | Public | Moderate | High (real-time) | Low | Not city-specific; forest focus only |
| ZEIMS (Zambia) | National | Restricted | Low | Periodic | None | No public map; outdated UI; no spatial visualization |
| GreenSpaces Map (UK) | National (UK) | Public | High | Moderate | Low | Data-intensive; context-specific; not adaptable |
| Lusaka Urban Greening | City-level | Limited | Low | Low | Minimal | No GIS dashboard; limited scalability; Lusaka only |
| iTree Platform | Global | Public | Moderate | Manual | None | Complex; not web-based; requires extensive data |
| **Proposed System (Kitwe)** | **City-level** | **Public** | **High** | **Regular** | **High** | **Designed for community data and GIS analytics** |

The comparison demonstrates that while several GIS systems exist globally, there is no open, web-based GIS platform specifically designed for mapping and managing urban green spaces in Kitwe. The proposed project addresses this gap by developing a locally adapted, scalable, and community-driven platform that combines the strengths of existing systems while addressing their limitations in the Zambian context.

### 2.5 Proposed System

The proposed system is a GIS-based web application that visualizes the spatial distribution of urban green spaces in Kitwe. The platform integrates geospatial data (shapefiles, satellite imagery, GPS coordinates) with a PostgreSQL/PostGIS database and visualizes it through Leaflet.js on an interactive web interface.

**Key Features:**

1. **Interactive Map Visualization**
   - Dynamic map display using Leaflet.js
   - Multiple base map options (OpenStreetMap, satellite imagery)
   - Zoom, pan, and layer control functionality
   - Filtering by green space type, size, and ward

2. **Spatial Data Management**
   - PostgreSQL database with PostGIS extension for spatial data storage
   - Support for multiple geometry types (points, polygons)
   - Attribute data management (name, type, area, ward, condition)
   - Data import/export capabilities

3. **Administrative Dashboard**
   - Secure login for authorized users
   - CRUD operations (Create, Read, Update, Delete) for green space records
   - Bulk data upload functionality
   - User management and access control

4. **Public Feedback Module**
   - Form for citizens to report new green spaces
   - Issue reporting for degraded or encroached areas
   - Photo upload capability
   - Status tracking for submissions

5. **Analytical Tools**
   - Summary statistics (total area, count by type)
   - Distribution analysis by ward
   - Accessibility metrics
   - Report generation (PDF/CSV export)

6. **Search and Filter Functionality**
   - Text search for green space names
   - Attribute-based filtering
   - Spatial search (find green spaces near a location)
   - Advanced query builder

**System Architecture:**

The system follows a three-tier architecture:

- **Presentation Layer:** HTML5, CSS3, JavaScript (Leaflet.js) for the user interface
- **Application Layer:** Python Flask framework for backend logic and API endpoints
- **Data Layer:** PostgreSQL with PostGIS extension for spatial data storage

**Integration with Open Data Sources:**

- OpenStreetMap for base maps and initial green space data
- Zambia Statistical Agency datasets for administrative boundaries
- GPS field surveys for ground-truthing and data validation
- Satellite imagery (Landsat 8) for vegetation analysis

The system's architecture is modular and scalable, allowing future expansion to other cities like Ndola or Lusaka. The use of open-source technologies ensures sustainability and reduces dependency on expensive proprietary software.

### 2.6 Summary / Conclusion

This chapter reviewed existing literature on urban green spaces, GIS applications, and web-based spatial systems. It identified key contributions from previous studies and highlighted limitations in current systems, particularly their lack of localization, citizen interactivity, and accessibility in the Zambian context.

The literature demonstrates that:

1. Urban green spaces provide critical environmental, social, and health benefits that justify investment in their management
2. GIS technology offers powerful tools for spatial data management and analysis
3. Web-based GIS systems improve accessibility and enable broader stakeholder participation
4. Existing systems, while valuable, do not adequately address the specific needs of Zambian cities like Kitwe

The proposed GIS-based web application for Kitwe bridges these gaps by providing a centralized, participatory, and dynamic mapping platform. The system aims to improve decision-making in urban environmental planning and foster public awareness of green space conservation.

The next chapter will detail the research methodology, including the software development approach, technologies employed, and data collection methods used to implement the proposed system.

---



## CHAPTER 3: RESEARCH METHODOLOGY

### 3.1 Introduction

This chapter outlines the research approach and methodology used to develop the Urban Green Space Mapping System for Kitwe. It describes the research design, selected software development methodology, data collection techniques, and technologies employed to accomplish the project's objectives.

The methodology chapter is structured to provide a clear understanding of: (1) the software development approach adopted, (2) justification for the chosen methodology, (3) technologies and frameworks used, (4) data collection and analysis methods, and (5) ethical considerations.

The selected methodology ensures that the system is built in a systematic, flexible, and efficient manner while addressing the specific requirements of geospatial data integration and visualization. This chapter demonstrates how theoretical concepts from software engineering and GIS are applied to create a practical solution for urban environmental management.

### 3.2 Selected Methodology (Agile Model)

#### 3.2.1 Overview of Agile Methodology

For this project, the **Agile Software Development Methodology** was chosen as the primary development approach. Agile emphasizes iterative development, continuous user feedback, and ongoing improvement throughout the development lifecycle (Beck et al., 2001). This methodology is particularly suitable for GIS-based systems where stakeholder requirements may evolve as new spatial data or insights become available during the development process.

Unlike traditional waterfall approaches that follow a rigid sequential process, Agile allows for flexibility and adaptation. The methodology is based on the principles outlined in the Agile Manifesto, which prioritizes:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

**Figure 4: Phases of Agile Methodology**

```
┌─────────────────────────────────────────────────────────────┐
│                    AGILE DEVELOPMENT CYCLE                   │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐      ┌──────────────┐      ┌───────────┐ │
│  │  Planning &  │ ───> │   Design &   │ ───> │Development│ │
│  │Requirements  │      │  Prototyping │      │           │ │
│  └──────────────┘      └──────────────┘      └───────────┘ │
│         ↑                                            │       │
│         │                                            ↓       │
│  ┌──────────────┐                          ┌──────────────┐ │
│  │  Review &    │ <─────────────────────── │   Testing &  │ │
│  │  Feedback    │                          │  Evaluation  │ │
│  └──────────────┘                          └──────────────┘ │
│                                                               │
│              (Iterations: Sprint 1, 2, 3, ...)               │
└─────────────────────────────────────────────────────────────┘
```

#### 3.2.2 Step-by-Step Agile Development Process

The development of the GIS web application followed an iterative Agile process divided into multiple sprints, each lasting 2-3 weeks. The following steps were followed:

**1. Requirement Gathering and Analysis (Sprint 0)**

- Conducted consultations with city planners from Kitwe City Council
- Interviewed environmental officers from ZEMA
- Engaged potential end-users to identify system requirements
- Collected baseline data on green spaces through open data portals (OpenStreetMap, Zambia Statistical Agency, Google Earth)
- Documented functional and non-functional requirements
- Created user stories and prioritized features

**2. System Design (Sprint 1)**

- Designed the system architecture (three-tier architecture)
- Created database schema for spatial and attribute data
- Developed wireframes for both administrative and public modules
- Designed user interface layouts and navigation flow
- Planned API endpoints and data flow
- Created use case diagrams and data flow diagrams

**3. Backend Development (Sprint 2)**

- Set up the development environment (PostgreSQL/PostGIS, Python Flask)
- Implemented database tables and spatial indexes
- Developed data ingestion modules to import shapefiles, GeoJSON, and CSV datasets
- Created RESTful API endpoints for CRUD operations
- Implemented authentication and authorization mechanisms
- Developed data validation and error handling

**4. Frontend Development (Sprint 3)**

- Developed interactive map using Leaflet.js
- Integrated map with backend via REST APIs
- Implemented filters, search functionality, and data visualization tools
- Created responsive design for mobile and desktop devices
- Developed administrative dashboard interface
- Implemented public feedback form

**5. Integration and Testing (Sprint 4)**

- Integrated all system components
- Conducted unit testing for individual modules
- Performed integration testing for API endpoints
- Executed user acceptance testing with stakeholders
- Evaluated system accuracy in displaying spatial data
- Tested responsiveness of the web interface

**6. Refinement and Optimization (Sprint 5)**

- Incorporated feedback from stakeholders
- Optimized database queries for performance
- Improved user interface based on usability testing
- Enhanced error handling and validation
- Added documentation and help features

**7. Deployment and Documentation (Sprint 6)**

- Deployed the system on a web server
- Configured production environment
- Created user manuals and technical documentation
- Provided training for administrators
- Established maintenance procedures

This iterative approach allowed flexibility to adjust to user feedback and improve functionalities after each cycle, ensuring that the final product met stakeholder expectations.

### 3.3 Justification of the Agile Software Development Model

The Agile methodology was chosen for this project due to several compelling reasons that align with the nature of GIS-based web application development:

**1. Flexibility and Adaptability**

GIS projects often involve evolving requirements as new spatial data becomes available or stakeholder needs change. Agile's iterative nature allows for continuous refinement and adaptation without disrupting the entire development process (Schwaber & Sutherland, 2017).

**2. Continuous Stakeholder Engagement**

Working with stakeholders such as the Kitwe City Council and ZEMA required regular feedback and validation. Agile's emphasis on customer collaboration ensured that the system remained aligned with user needs throughout development (Beck et al., 2001).

**3. Early and Frequent Delivery**

Agile enables the delivery of working software increments at the end of each sprint. This allowed stakeholders to see progress early and provide feedback before significant resources were invested in potentially incorrect directions (Pressman, 2014).

**4. Risk Mitigation**

By breaking the project into smaller iterations, risks were identified and addressed early. Technical challenges with spatial data integration or mapping libraries could be resolved in one sprint without affecting the entire project timeline (Sommerville, 2016).

**5. Parallel Development**

Agile supports parallel development of different system components. While the database was being designed, frontend prototypes could be developed using mock data, accelerating the overall development timeline.

**6. Compatibility with Open-Source Technologies**

The project relies heavily on open-source tools (PostgreSQL, Flask, Leaflet.js) that have active communities and frequent updates. Agile's flexibility allows for incorporating new features or addressing compatibility issues as they arise.

**7. Better Quality Through Continuous Testing**

Agile emphasizes testing throughout the development cycle rather than as a final phase. This approach resulted in higher code quality and fewer defects in the final product (Pressman, 2014).

**Comparison with Alternative Methodologies:**

- **Waterfall Model:** Too rigid for a project where requirements might evolve based on data availability and stakeholder feedback
- **Spiral Model:** More complex than necessary for a project of this scope and timeline
- **Rapid Application Development (RAD):** Suitable but less structured than Agile for managing multiple stakeholders

Therefore, Agile offered the ideal framework for an iterative, user-centered development process that balanced structure with flexibility.

### 3.4 Technologies and Frameworks Used

The development of the GIS-based web application leveraged a comprehensive stack of open-source technologies, each selected for its specific capabilities, community support, and suitability for geospatial applications.

#### 3.4.1 Programming Languages

**JavaScript**
- **Purpose:** Client-side interactivity and map visualization
- **Usage:** Implementing interactive map features using Leaflet.js, handling user events, AJAX requests to backend API
- **Version:** ES6+ (ECMAScript 2015 and later)
- **Justification:** Universal browser support, extensive library ecosystem, essential for web-based GIS applications

**Python (Version 3.9+)**
- **Purpose:** Backend logic and API development
- **Framework:** Flask (lightweight web framework)
- **Usage:** RESTful API endpoints, database operations, data processing, authentication
- **Justification:** Excellent support for geospatial libraries (Shapely, Fiona), clean syntax, rapid development

**HTML5 and CSS3**
- **Purpose:** Web interface structure and styling
- **Usage:** Page layout, responsive design, visual presentation
- **Frameworks:** Bootstrap 5 for responsive grid system and UI components
- **Justification:** Modern web standards, cross-browser compatibility, mobile-first design

**SQL (Structured Query Language)**
- **Purpose:** Database queries and spatial operations
- **Extension:** PostGIS spatial SQL functions
- **Usage:** Spatial queries, data retrieval, aggregations
- **Justification:** Standard database language with powerful spatial extensions

#### 3.4.2 Database

**PostgreSQL with PostGIS Extension**

- **Version:** PostgreSQL 13.x with PostGIS 3.1
- **Purpose:** Storing spatial data (coordinates, polygons) and attribute data (green space characteristics)
- **Key Features:**
  - Advanced GIS functions (spatial indexing, geometric analysis)
  - Support for multiple geometry types (Point, LineString, Polygon, MultiPolygon)
  - Spatial reference system transformations
  - Efficient spatial queries (ST_Contains, ST_Intersects, ST_Distance)
  - ACID compliance for data integrity

**Database Schema:**

The database consists of the following main tables:

1. **green_spaces** - Core table storing green space data
   - id (Primary Key)
   - name (VARCHAR)
   - type (VARCHAR) - park, garden, forest, sports_field
   - area_sq_m (FLOAT)
   - ward (VARCHAR)
   - geom (GEOMETRY) - spatial column
   - created_at (TIMESTAMP)

2. **public_feedback** - User submissions
   - id (Primary Key)
   - green_space_id (Foreign Key)
   - user_name (VARCHAR)
   - user_email (VARCHAR)
   - issue_type (VARCHAR)
   - description (TEXT)
   - status (VARCHAR) - pending, reviewed, resolved
   - created_at (TIMESTAMP)
   - location (GEOMETRY)

3. **users** - Administrative users
   - id (Primary Key)
   - username (VARCHAR)
   - email (VARCHAR)
   - password_hash (VARCHAR)
   - user_type (VARCHAR)
   - created_at (TIMESTAMP)

**Justification:** PostgreSQL with PostGIS is the industry standard for open-source spatial databases, offering robust performance, reliability, and comprehensive spatial functionality (PostGIS Documentation, 2023).

#### 3.4.3 GIS Tools and Libraries

**Leaflet.js (Version 1.9.x)**
- **Purpose:** Interactive web mapping library
- **Features:**
  - Lightweight (39 KB of JavaScript)
  - Mobile-friendly with touch support
  - Layer control and overlays
  - Marker clustering for performance
  - Custom popup and tooltip styling
- **Justification:** Open-source, well-documented, extensive plugin ecosystem, excellent performance

**OpenStreetMap (OSM)**
- **Purpose:** Base map tiles and initial green space data
- **Usage:** Background map layers, street networks, building footprints
- **API:** Tile server for map rendering
- **Justification:** Free, open data, community-maintained, global coverage

**QGIS (Version 3.22+)**
- **Purpose:** Desktop GIS tool for data preprocessing
- **Usage:**
  - Digitizing green space boundaries
  - Data cleaning and validation
  - Coordinate system transformations
  - Exporting data to formats compatible with PostGIS
- **Justification:** Free, powerful, supports multiple data formats, excellent for data preparation

**Shapely (Python Library)**
- **Purpose:** Geometric operations in Python
- **Usage:** Validating geometries, calculating areas, spatial relationships
- **Justification:** Integrates well with PostGIS, Pythonic interface for geometric operations

**Fiona (Python Library)**
- **Purpose:** Reading and writing spatial data formats
- **Usage:** Importing shapefiles, GeoJSON, and other vector formats
- **Justification:** Simple API, efficient, works seamlessly with Shapely

#### 3.4.4 Web Server and Hosting

**Flask Development Server (Development)**
- **Purpose:** Local testing and development
- **Features:** Auto-reload, debugging tools, simple configuration

**Gunicorn (Production)**
- **Purpose:** WSGI HTTP server for production deployment
- **Features:** Process management, load balancing, stability
- **Configuration:** Multiple worker processes for concurrent requests

**Nginx (Reverse Proxy)**
- **Purpose:** Web server and reverse proxy
- **Features:**
  - Static file serving
  - SSL/TLS termination
  - Load balancing
  - Caching
- **Justification:** High performance, low resource usage, industry standard

#### 3.4.5 Development Tools

**Visual Studio Code (IDE)**
- **Purpose:** Code editor and development environment
- **Extensions:** Python, JavaScript, HTML/CSS, Git integration
- **Justification:** Free, lightweight, excellent extension ecosystem

**Git and GitHub**
- **Purpose:** Version control and collaborative development
- **Usage:** Code versioning, branch management, backup
- **Justification:** Industry standard, facilitates collaboration, free hosting

**Postman**
- **Purpose:** API testing and documentation
- **Usage:** Testing REST endpoints, debugging API responses
- **Justification:** User-friendly, supports automated testing, documentation generation

**pgAdmin 4**
- **Purpose:** PostgreSQL database administration
- **Usage:** Database management, query execution, schema visualization
- **Justification:** Official PostgreSQL tool, comprehensive features

#### 3.4.6 Hardware and Software Requirements

**Development Environment:**

| Category | Minimum Requirement | Recommended |
|----------|-------------------|-------------|
| Processor | Intel i5 or equivalent | Intel i7 or equivalent |
| Memory | 8 GB RAM | 16 GB RAM |
| Storage | 500 GB HDD | 1 TB SSD |
| Operating System | Windows 10/11, Linux, macOS | Ubuntu 20.04 LTS or Windows 11 |
| Internet | Broadband connection | High-speed broadband |

**Software Stack:**

- PostgreSQL 13+ with PostGIS 3.1+
- Python 3.9+
- Node.js 14+ (for package management)
- QGIS 3.22+
- Web browser (Chrome, Firefox, or Edge)
- Git 2.30+

#### 3.4.7 Data Sources

The system integrates data from multiple sources to create a comprehensive green space inventory:

**1. OpenStreetMap (OSM)**
- **Type:** Crowdsourced geographic data
- **Usage:** Base maps, initial green space boundaries, street networks
- **Format:** XML, PBF (Protocol Buffer Format)
- **Access:** Free download via Overpass API

**2. Zambia Environmental Management Agency (ZEMA)**
- **Type:** Official environmental data
- **Usage:** Protected areas, environmental zones
- **Format:** Shapefiles, PDF reports
- **Access:** Obtained through official request

**3. Kitwe City Council**
- **Type:** Municipal administrative data
- **Usage:** Ward boundaries, zoning information, official park records
- **Format:** Shapefiles, Excel spreadsheets
- **Access:** Provided by city planning department

**4. GPS Field Surveys**
- **Type:** Primary data collection
- **Usage:** Ground-truthing, new green space identification, attribute verification
- **Tools:** Mobile GIS apps (QField, Locus Map)
- **Format:** GPX, GeoJSON

**5. Satellite Imagery**
- **Type:** Remote sensing data
- **Source:** Landsat 8, Sentinel-2
- **Usage:** Vegetation classification, change detection
- **Format:** GeoTIFF
- **Access:** Free download via USGS Earth Explorer

### 3.5 Data Collection and Analysis

#### 3.5.1 Data Collection Methods

The project employed a mixed-methods approach to data collection, combining primary and secondary data sources:

**Primary Data Collection:**

1. **GPS Field Surveys**
   - Conducted field visits to 25 known green spaces in Kitwe
   - Recorded GPS coordinates using mobile devices
   - Captured photographs for documentation
   - Collected attribute data (name, type, condition, facilities)
   - Validated boundaries by walking perimeters

2. **Stakeholder Interviews**
   - Semi-structured interviews with 5 city planners from Kitwe City Council
   - Discussions with 3 environmental officers from ZEMA
   - Informal conversations with 10 residents about green space usage
   - Documented requirements and expectations for the system

3. **Observational Studies**
   - Site visits to assess green space conditions
   - Documentation of encroachment and degradation
   - Observation of public usage patterns

**Secondary Data Collection:**

1. **OpenStreetMap Data**
   - Downloaded OSM data for Kitwe using Overpass API
   - Extracted features tagged as parks, gardens, forests
   - Obtained 35 initial green space records

2. **Government Records**
   - Obtained ward boundary shapefiles from Kitwe City Council
   - Collected historical maps and planning documents
   - Reviewed environmental reports from ZEMA

3. **Satellite Imagery**
   - Downloaded Landsat 8 imagery for Kitwe (2020-2024)
   - Processed imagery for vegetation indices (NDVI)
   - Used for visual interpretation and validation

4. **Academic Literature**
   - Reviewed research papers on urban green spaces in Africa
   - Studied GIS methodologies and best practices
   - Examined similar projects in other cities

#### 3.5.2 Data Analysis Techniques

**Spatial Analysis:**

1. **Buffer Analysis**
   - Created buffer zones around green spaces to assess accessibility
   - Analyzed population coverage within 500m walking distance
   - Used PostGIS ST_Buffer function

2. **Overlay Analysis**
   - Overlaid green spaces with ward boundaries
   - Calculated green space distribution by administrative area
   - Used PostGIS ST_Intersects and ST_Intersection functions

3. **Proximity Analysis**
   - Calculated distances between green spaces
   - Identified underserved areas with limited access
   - Used PostGIS ST_Distance function

4. **Area Calculations**
   - Computed total green space area per ward
   - Calculated per capita green space availability
   - Used PostGIS ST_Area function

**Attribute Analysis:**

1. **Descriptive Statistics**
   - Calculated mean, median, and standard deviation of green space sizes
   - Determined frequency distribution by type
   - Generated summary reports

2. **Categorization**
   - Classified green spaces by size (small <1 ha, medium 1-5 ha, large >5 ha)
   - Grouped by type (park, garden, forest, sports field)
   - Assessed condition (good, fair, poor)

**Visual Analysis:**

1. **Map Visualization**
   - Created thematic maps showing green space distribution
   - Generated heat maps of green space density
   - Produced choropleth maps of per capita availability

2. **Chart Generation**
   - Bar charts showing green space count by ward
   - Pie charts illustrating type distribution
   - Line graphs depicting temporal changes

**Data Quality Assessment:**

1. **Completeness Check**
   - Verified that all required attributes were populated
   - Identified and addressed missing data

2. **Accuracy Validation**
   - Cross-referenced GPS coordinates with satellite imagery
   - Validated boundaries through field verification
   - Checked attribute accuracy with local knowledge

3. **Consistency Verification**
   - Ensured uniform naming conventions
   - Standardized type classifications
   - Validated geometry topology

### 3.6 Ethical Considerations

The project adhered to ethical research practices and data protection principles:

**1. Data Privacy and Confidentiality**
- Personal information from feedback submissions is stored securely
- User email addresses are not publicly displayed
- Administrative access is restricted to authorized personnel only

**2. Data Source Authorization**
- All data obtained from open and authorized sources
- Proper permissions obtained from Kitwe City Council and ZEMA
- OpenStreetMap data used in compliance with Open Database License (ODbL)

**3. Intellectual Property**
- Proper citation and acknowledgment given to all data providers
- Open-source licenses respected for all software components
- Original work clearly distinguished from existing resources

**4. Privacy Protection**
- Private property information not collected or displayed without consent
- No personally identifiable information collected from public users
- Feedback submissions are anonymous by default (optional name/email)

**5. Responsible Use**
- Data used strictly for academic and environmental management purposes
- No commercial exploitation of collected data
- Results shared with stakeholders for public benefit

**6. Informed Consent**
- Stakeholders informed about the purpose and use of interviews
- Participants in field surveys provided verbal consent
- Users informed about data collection through privacy policy

**7. Environmental Responsibility**
- Field surveys conducted with minimal environmental impact
- No damage to green spaces during data collection
- Promotion of conservation through the system

### 3.7 Summary / Conclusion

This chapter outlined the comprehensive methodology employed in developing the Urban Green Space Mapping System for Kitwe. The Agile software development methodology was selected for its flexibility, iterative nature, and emphasis on stakeholder collaboration, making it ideal for a GIS-based project with evolving requirements.

The technology stack, comprising PostgreSQL/PostGIS, Python Flask, Leaflet.js, and QGIS, was carefully chosen to provide robust spatial data management, efficient backend processing, and interactive frontend visualization. The use of open-source technologies ensures sustainability, cost-effectiveness, and community support.

Data collection combined primary methods (GPS surveys, stakeholder interviews) with secondary sources (OpenStreetMap, government records, satellite imagery), resulting in a comprehensive dataset of 35 green spaces. Spatial and attribute analysis techniques were applied to derive meaningful insights about green space distribution and accessibility.

Ethical considerations were carefully addressed, ensuring data privacy, proper authorization, and responsible use of information. The methodology provides a solid foundation for the system analysis, design, and implementation phases detailed in subsequent chapters.

The next chapter will present the system analysis and design, including functional requirements, use case diagrams, data flow diagrams, and architectural design that translate the methodology into a concrete system blueprint.

---

