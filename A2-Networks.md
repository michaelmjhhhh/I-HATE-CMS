# A2 Network Fundamental

## A2.1.1 Describe the purpose and characteristics of networks 
--- 
- Local Area Network (LAN)
  - connects network devices over a short distance 
  - LANs are designed to operate distances not exceeding approximately 1km
  - longer distances will result in latency

  - LANs are characterized by high data transfer rates and relatively low latency
  - LANS can be both wired or wireless, but are usually a mix of two 

  > The primary goal of LAN is to facilitate the sharing of resources such as files, printers, and software applications among multiple users in a local area.


- Wide Area Network (WAN)
  - a WAN connects network devices across larger geographic areas that can span cities, countries, and even continents. 
  - WANs are characterized by their ability to maintain reliable data communication over longer distances, comparing to LAN.
  - However, WANs often have lower data transfer rates and higher latency than LANs, because the primary goal is to enable communication among long distances. 

  - The default and primary purpose for WANs is to enable businesses, governments, and other entities to operate on a wide scale. 
  - WANs facilitate the connection of smaller, geographically dispersed networks such LANs and MANs in to a **cohesive system**, allowing for **centralized data processing, collaborative work, and access to shared resources regardless location.**

  - WANs can be established over leased lines or satellite links, or through public internet connections through VPNs to ensure security and privacy. 

- Personal Area Network (PAN)
  - PAN is designed for personal use and usually spans no more than 10 meters. 
  - This range is optimal for devices **centred around a single person's workspace or within their immediate physical environment**.

  - PANs are characterized by their **convenience for inter-device communication on a such small scale, facilitating direct interaction between personal devices such as phones, computers, printers, smart watches and wearable devices.**

  > The primary goal of a PAN is to enable the connection and communication of personal devices for individual use, streamlining the sharing of data and access to personal resources like contacts, internet access, and multimedia files. This network type enhances personal productivity and entertainment by allowing seamless device synchronization, data transfer and internet sharing in a highly localized setting.

  
  - Examples of PAN usage include:
    - connecting a smartphone to wireless headphone for music streaming
    - syncing a laptop with a mouse and keyboard
    - connecting a smartphone to a smartwatch for fitness tracking


  - PANs can be established using **wireless technologies such as Bluetooth and WIFI Direct**. 
    - which are specifically designed for short range communication and require minimal power, making them ideal for personal device connectivity. 


- Virtual Private Network (VPN)
  - A virtual private network (VPN) **extends a private network across a public network**, allowing users **to send and receive data as if their devices were directly connected to the private network**. 
  - A VPN can function over **unlimited distances** since it **uses the internet to create a secure and encrypted connection between devices and the private network**. 
    - This encryption ensures that **data transmitted over the VPN is protected from unauthorized access.**


  - The primary goal of a VPN is to **provide secure remote access to a private network and its resources**, such as files, printers, and software applications, **from any location with internet access**. Remote workers, organizations with global operations, and individuals concerned with privacy and security online all benefit from VPNs. 
  - **By creating a “tunnel” through the public internet that encrypts data as it travels back and forth**, VPNs ensure that sensitive information **remains confidential and secure from potential cyber threats**.

  - Examples of VPN usages include:
    - employees access to their **company's internal servers and documents securely while working from home.**
      - They can access to their company's **private network** directly and securely.
    - individuals browsing the internet privately without revealing their **IP address or location**
      - This is because the encryption ensures that data transmitted over the VPN tunnel is protected, and cannot view by others without proper authorization.
    - connecting to a geo-restricted content by appearing to be in a different geographical location
      - A VPN **routes user traffic through a remote server in another geographical location**, **replacing the user’s IP address with that server’s IP**. As a result, websites identify the user as being in that location, allowing access to geo-restricted content.
      - **The VPN server acts as a gateway to the private network. A secure encrypted tunnel is established over the public network, and all traffic is routed through the VPN server, making it appear as if the user’s IP address is that of the server.**


## A2.1.3 Describe the function of network devices
--- 
- Gateways 
  - Gateways are network devices that act as a bridge between two networks that use disparate protocol. 
  - A device that connects two different networks and allows data to pass between them.

  - A gateway can **enable communication between an office network and the internet**, **converting private network addresses to a public address using protocols such as NAT (network address translation)**. 
  - Additionally, gateways might **incorporate security functions, filtering, and traffic management to enhance data flow and security across the networks they bridge.**
  - A gateway can also be used to **convert data between different network protocols**.
    - For example, a gateway might translate email traffic from the simple mail transfer protocol (SMTP) on an enterprise network to another messaging protocol used by an external network, **facilitating seamless communication between different email systems.**
    - **Gateway can convert between different protocols.**


  - Within the context of voice over internet protocol (VoIP) communications, a gateway **can translate between the digital signals used within an IP network and the analogue signals of traditional phone lines.**
    - This enables calls to be made between internet-based VoIP users and traditional telephone users.

  > An example: If you use Wechat to call landline, gateway is being used here.


- Hardware firewalls
  - Firewalls are **network security devices that monitor and control incoming and outgoing network traffic (packets) based on predetermined security rules.** 
  - A firewall typically **establishes a barrier between a trusted internal network and untrusted external networks**, such as the internet, to **block malicious traffic and prevent unauthorized access**.

  - Key features and functions
    - monitoring packets and data
    - prevent malicious data, packets and traffic
    - allow safe and legitimate packets, data, and traffic

  - Usage Scenarios
    - Prevent attack/Direct interception 直接拦截
      - from skeptical IP address
      - contains malicious data packets

    - Quality of Service (QoS)
      - Zoom/VoIP(voice over internet protocol) or other important services **higher priority**
      - game **lower priority**
      - reduce latency and optimize experience 

    - Family Scenario 
      - routers contain firewall
      - prevent the potential threat form hacker 
      - parent control(restrict websites) 

  - Software and hardware firewalls

  | Category        | Software Firewall              | Hardware Firewall              |
  |-----------------|-------------------------------|--------------------------------|
  | Location        | On a single device            | At the network gateway         |
  | Scope           | One computer                  | Entire network                 |
  | Flexibility     | High (customizable)           | Lower                          |
  | Protection Area | Internal threats              | External attacks               |
  | Example         | Windows Defender              | Router / Enterprise firewall   |

  > A firewall is a network security device that monitors and controls incoming and outgoing traffic based on predefined rules, protecting a network from unauthorized access and malicious attacks.


- Modems 
  - Modems stands for the **modulator-demodulator**.

  > Modems (modulator–demodulators) are devices that **facilitate data transmission over telephone lines or broadband connections by converting digital data from a computer into analogue signals suitable for sending over these lines, and vice versa**. They serve as a **bridge between the digital data networks and analogue phone systems**.

  - Modulator is used for transferring the digital signals(0,1) from a computer to analogue signals.
  - Demodulator is used for transferring the analogue signals to digital signals. 


  - ![modem](./typora-user-images/modem.png)

  

  - ![modems-usage-scenarios](./typora-user-images/modem2.png)

  
  - **A modem converts digital signals into analogue signals for transmission over communication lines and converts them back into digital signals at the receiving end.**


- Network interface cards (NICs)
  - Network interface cards (NICs) are hardware components within a computer or network device which **facilitate the interface between the physical network and the device’s processing capabilities.**
  - NICs **perform the critical function of converting electrical signals received from the network into digital data that the computer’s processor can understand and vice versa. This conversion is essential for the communication process over computer networks.**

  > A NIC connects a device to a network by converting signals into digital data, transmitting and receiving packets, and using a MAC address to ensure correct delivery.

  - characteristics
    - connect 
      - enables the device to connect to network 
    - convert 
      - convert electrical/light/radio signal to digital data, or vice versa 
    - transmit/receive
      - send or receive data (bidirectional)
    - identify MAC address
      - MAC address uniquely identifies each device
      - ensure that packages are being sent to the correct/intended device
    - protect 
      - buffer: prevent package loss 
      - CRC: error checking 

- Router 
  - Routers are **network devices that manage the exchange of data between different networks. They direct data packets by determining the optimal path for transmission using routing tables and routing protocols.**
  - At its core, a router **examines the destination IP address in each packet and uses a routing table to determine the best next hop**. Routers update their routing tables using static or dynamic routing protocols, allowing them to learn network paths and make efficient routing decisions.

  - Routers are responsible for receiving, processing, and forwarding data packets to their correct destinations. A packet may pass through multiple routers before reaching its destination. Routers inspect packet headers and use protocols such as RIP (Routing Information Protocol) to find the fastest path.

  - Key Functions
    - Determine the best path for data transmission
    - Forward packets between networks
    - Use IP addresses to identify destinations
    - Maintain routing tables
    - Use routing protocols (e.g., RIP) to update paths


  > A router directs data packets between networks by using IP addresses and routing tables to determine the best path.
  > A router can establish a connection between LAN and WAN.


- Switches 
  - **Switches are networking devices that connect devices within a LAN. Switches manage the flow of data within a network by receiving, processing and forwarding data packets (also called frames) to the correct destination device.**

  - At their core, switches receive incoming data packets from one device and **use the MAC address information contained within the packet to forward it to the appropriate destination device.**

  - Switches **maintain a MAC address table**, also known **as a forwarding table**, which **maps each MAC address to the corresponding switch port**. This allows the switch to effectively direct traffic by looking up the destination MAC address of each frame and forwarding the frame directly to the port associated with that address.

  - While switches are efficient at **directing traffic**, they must **handle broadcasts (sent to all devices) and multicasts (sent to a group of devices) differently**. For these types of traffic, the switch forwards the frames to multiple ports based on the needs of the network protocol being used.


| Scenario                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Small / Home Office    | Connects devices (computers, printers, storage) and enables resource sharing |
| Enterprise Networks    | Supports VLAN segmentation, link aggregation, improves security & performance |
| Data Centres           | Manages server traffic, high throughput, low latency, handles large data     |
| Schools / Universities | Connects campus networks, supports thousands of devices                      |


- Wireless access points (WAPs)
  - **Wireless access points (WAPs) serve as the interface between the wired infrastructure and wireless devices. WAPs convert wired Ethernet data into wireless signals and vice versa, effectively extending the reach of the network to areas where wiring is impractical, impossible or undesirable.**

  - **WAPs broadcast wireless signals that wireless devices can detect and connect to. They operate by receiving data packets from the wired network, converting these packets into radio frequencies, and transmitting them wirelessly. The process is reversed for incoming signals from wireless devices, which are converted back into data packets and relayed onto the wired network.**

  - In larger installations, multiple WAPs can be configured to create a wireless network mesh. This setup allows users to move between different areas (for example, between floors or rooms in a building) without losing connection, as their devices automatically switch to the strongest available signal from the nearest WAP.

  - WAPs can be managed centrally, often via controllers that configure settings, manage network policies and provide tools for monitoring network usage and performance. This central management helps maintain consistent configurations across multiple WAPs and simplifies the task of updating network settings or firmware.


| Scenario                | Function                                      | Benefits                                      |
|------------------------|-----------------------------------------------|-----------------------------------------------|
| Office                 | Wireless access across building               | Mobility, collaboration                        |
| Schools / Universities | Campus-wide wireless coverage                 | Access from classrooms, libraries, outdoors    |
| Public / Retail        | Provide free Wi-Fi                            | Customer satisfaction, location-based services |
| Residential            | Home wireless connectivity                    | Supports multiple smart devices                |




- How devices map to the layers of the TCP/AP model 

![devices-map-to-the-layers-of-the-TCP/AP-model](./typora-user-images/map.png)











    


















  


    






