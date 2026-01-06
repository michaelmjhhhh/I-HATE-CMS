---
sidebar_position: 1
title: A1 Computer Fundamentals
---

# A1 Computer Fundamentals

## A1.1.1 Describe the functions and interactions of the main CPU components

### CPU

- is the primary computational(计算的) engine of the computer, responsible for executing instructions.

- it is a hardware component(组成部分) that performs 

  - **Arithmetic (算数，计算)**
  - **Logical or input/output operations**, in order to process data from input devices into useful information. 

- Block Diagram of CPU

  - ![截屏2025-11-21 10.33.10](./assets/%E6%88%AA%E5%B1%8F2025-11-21%2010.33.10.png)

- **Key Components of CPU**

  - Component refers to a distinct functional unit or part within the CPU that has a specific role in the processors operation.
  - **Control Unit (CU)**
  - **Arithematic Logic Unit (ALU)**
  - **Registers (寄存器)**
    - IR, PC, MAR, MDR, CIR, AC
  - **Cache (高速缓存)**
    - L1,L2,L3
  - **Buses (总线)**
    - Control Bus 
    - Data Bus
    - Address Bus

- **Control Unit**

  - Responsible for orchestrating the **fetch-decode-execute cycle**. lts primary functions include **decoding and interpreting instructions fetched from** **memory** and **generating control signals** to **activate the hardware units** within the CPU. This involves **parsing(解析)** the instructions opcode (operation code), which determines the **specific action** such as reading data, writing data, performing calculations or testing logic. 

- **Arithmetic Logic Unit (ALU) 算数逻辑单元**

  - Performs **arithmetic and logical operations**. It is where the **actual computation happens**, such as addition, subtraction, and logical operations like AND, OR, NOT, and so on. 

  - **Works with the** **Accumulator** **(ACC)** or **general-purpose registers** to store results. 

    - ACC是累加器，作用有

    - **暂存中间结果**：它专门用于**暂时存放算术逻辑单元 (ALU)** 运算的**中间结果**。

      **隐含操作数**：在许多 CPU 指令中，累加器被作为运算的一个**隐含操作数**。

      - **例如：** 在执行一个简单的 `ADD X`（加 X）指令时，CPU 会将内存地址 X 中的值取出，然后**与累加器 (ACC)** 中当前的值相加，并将最终的结果重新存回 **ACC** 中。

  - **Receives control signals** from the Control Unit (CU) telling it which operation to do. 



- **Registers 寄存器 **

  - A register is a **small-capacity, very fast storage** **location available** within the CPU, used to store data **temporarily** during the execution of programs. It is capable of **holding instructions, storage addresses or data.** 
  - Common register includes
    - **PC(Program Counter)**: Holds the **address** for the next instruction. It is incremented automatically after each instruction is executed(the most common way is to say that it is incremented at the end of the fetch phase), pointing to the next instruction in the program's memory location. 指向了 CPU 接下来要从主内存 (RAM) 中取出的那条指令。
    - **IR(Instruction Register)**: Holds the **current** instruction being executed. It acts as a temporary holding area for the instruction before it is decoded and executed. (decode and execute will be discussed later.)
    - **MAR (Memory Address Register)**: 
      - Stores the **address in memory** where **the next piece of data or instruction** is to be found or stored. 
      - **MAR** can also hold the **destination address** where processed data should be stored in the memory.
      - To enable communication between the **MAR** and **primary memory**, a **connection via the Address Bus** is used. Bus will be discussed later. 
    - **MDR (Memory Data Register)**: 
      - MDR **holds the data** **or instruction** that is **being transferred** **to or from** primary memory. 存的数据或者指令，可以是从memory fetch过来的，也可以是即将要store进memory中某一个地方的data
      - MDR works closely with the **MAR**; the **address in the MAR** determines which data is **loaded** into the MDR. loaded就是拿到memory对应address中的instruction/data，然后通过data bus存进MDR的过程
      - After processing, the **ALU places the result into the MDR**, which is then **written to the RAM** at the address specified by the MAR.
      - The **Data Bus** enables the transfer of data between **RAM and the MDR**. 
    - **ACC(Acumulator)**: A special-purpose register used to store **intermediate results of operations**. It is often used for arithmetic and logical operations. It can also be used as a temporary storage Accumulator (AC) | location for other data. ALU的专用register.
  
- **Buses 总线**

  - A bus is a shared communication pathway which **transfers data** between components within a computer. 

  - 和Bus有关的，就不局限于CPU，而是整个计算机主板或者外部的设备，因此之后的components就不是cpu内部的组件了, CPU内部组件的data transfer使用的是一个叫做internal bus的东西 

    - Control Bus

      - Carries **control signals (not actual data)** from the **Control Unit (CU)** to other components, managing actions and timing. 
    - It can be unidirectional or bidirectional. 可是单向，也可以是双向。
      - Handles commands like **read/write, interrupts, timing, and acknowledgments.**
  
    - Data Bus 

      - A pathway for transferring **actual data** between the CPU, memory, and other components. 
    - Width affects speed (e.g., 32-bit vs 64-bit)
      - Bidirectional (data flows both ways). 既可以从CPU到components，这是一个store，也可以components到cpu，这是一个load
  
    - Address Bus

      - A pathway which carries **memory addresses** from the CPU to specify **where data should be read or written.** It's `where`, so the address bus carries address.

      - Address Bus is unidirectional, only the CPU sends memory address to components.

        

- **Types of CPU processors**

- Key terms you need to know first: 

- Parallel processing: A computing technique in which **multiple processors or cores** within a **single machine, or across multiple machines,** **simultaneously** execute **different parts of a task or multiple tasks to improve the overall speed and efficiency** of computation. 

- Architecture:  The **design and organization** of a computer systems hardware and software components. This includes the structure and functionality to 

  perform computational tasks. 

  - Single-core processor:
    - A single-core processor possess(拥有) **one processing unit (core)** integrated into a single circuit. This core is the fundamental unit that reads and executes instructions from processes. With a **singular processing path**, it handles one instruction at a time, following a **sequential execution** model.
    - This architecture was standard in **early CPUs and older computers**, where task completion relied **on the linear processing of instructions.** 
    - Its primary limitation is in **executing parallel processing demands**. As computational tasks become more complex and **multitasking** becomes essential, single-core processors face limitations in performance, leading to potential bottlenecks(瓶颈) in processing efficiency. 
  - Multi-core processor:
    - A multi-core processor is a **single computing component(a single chip**) that contains **two or more independent processing cores**, each capable of **executing instructions in parallel.** 
    - This architecture enables the processor to **handle multiple instructions at once(due to multi-core)**, significantly improving performance(faster) over single-core designs, especially for **multitasking and parallel processing tasks.**
    - Ideal for multitasking, gaming, and servers
    - Software must be specifically written to take advantage of the **multiple cores to see performance benefits.**
    - They offer improved **performance and efficiency** by **distributing workloads across multiple processing units(distibute a big task to sub-tasks, and each task is completed by a processing unit(core) inside the computing component(chip) simultaneously.**
  - Co-processor:
    - are specialized processors designed to **supplement** the main CPU, **offloading(分流) specific tasks** to optimize performance. Co-processor can be **integrated into CPU or exist as seperate entites**. Co-processors **free the main CPU** to focus on **general processing tasks.** 
    - This is a processor with a specific job to support the main CPU. Allows tasks to **run in parallel**, enhancing overall system performance.
    - Examples include Graphics Processing Units (GPUs), audio processors, and Digital Signal Processors (DSPs). 
    - When accomplishing these tasks, co-processors may be used:
      - graphics rendering, mathematical calculations, or data encryption(加密)

## A1.1.2 Describe the role of GPU

> GPU stands for graphics processing unit, a specialized electronic circuit **containing numerous processing units.** 

**Features of GPU**

- GPU processes **highly parallel structure**, ideal for **complex graphic calculations.** 
- GPU can be **intergrated** inside CPU, or **descrete**(a seprate card).
- GPU communites with software using APIs like DirectX or OpenGL.
- Not only for processing and rendering graphics, GPU is increasingly used for **machine learning** and other **computationally intensive workloads.** 

**GPU architecture** 

- GPU has a **distinct architecture** which sets them apart from conventional CPUs, and allows them to process **large blocks of data cocurrently**(同时的), leading to more efficient processing for certain types of tasks.  

| GPU Features                  | Characteristic                                               | Example                                                      |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Parallel Processing Abilities | GPU has thousands of small cores designed for parallel computing | Can process multiple pixels at the same time, significantly reducing the time required to apply the filter to the entire image |
| High Throughput(吞吐量)       | GPU is optimized for high throughput, meaning that it can process a large amount of data simultaneously. This feature is especially useful for graphic rendering and complex calculations | In graphic rendering like video games or 3D simulations, high throughput allows it to process and display complex scenes in real time. It can calculate the color, position and texture of thouthands of pixels cocurrently, enabling detailed graphics. |
| Memory                        | GPUs are equipped with high speed memory(VRAM), which handles the large data sets and textures, required in high resolution video rendering and complex scientific calculations. | GPU requires on VRAM (high-speed memory) to store and manage the textures of large data sets for rendering scenes. The high speed allows fast manipulations of this data, enabling the rendering for high-resolution videos in real-time without buffering and delays |

**Real World Applications of GPU**

- rendering complex graphic in video games

  - rendering high resolution textures, realistic lighting effects and smooth frame effects. 
  - enhancing the gaming experience, providing higher frame rates, and off-loading rendering work from the CPU. 

- AI and machine learning

  - faster process of large data sets
  - the training process of ML model involves extensive matrix multiplications(multidimensional) and other operations which can be parallelized effectively on a GPU

- Scientific computing and large simulations

  - quicker computations in physics simulations and climate modelling 

- Graphic design and video editing

  - epecially in the creation of 3D models and environments, GPU enables designers to visualize their work in real-time

  - Using softwares like Blender, GPUs are utilized to render complex scenes, including lighting effects, shadows and textures, in real-time(实时的). 

    

## A1.1.3 Explain the differences between the CPU and the GPU (HL only)



### Design Philosophy and usage scenarios



#### Design Philosophy

- **CPU**
  - The design philosophy of CPUs emphasizes **flexibility and generalizability**, enabling CPUs to efficiently process a **wide variety** of instructions and data types. It's generalized. 
  - CPUs are also designed for **low latency**, meaning they prioritize getting things done quickly, even if it is just one task at a time. 
  - These features mean that CPUs often have **smaller number of cores**, but each core is **very poweful** with features such as **larger caches** and **complex logic units**. This allows CPUs to handle a wider variety of instructions efficiently. 
  - Another design philosophy for CPUs is to focus on **branch prediction(分支预测)**. CPUs excel at **predicting which instruction** will be needed **next and fetching it in advance**. This **minimizes** wasted time and keeps the core running **smoothly**. 
    - **Branch prediction**: Because the CPU is incredibly fast, fetching instructions from memory feels slow comparing to the CPU.  If the CPU waits for every `if` condition to finish before fetching the next instruction, the core would waste many cycles doing nothing. So instead, it **guesses** whether the program will take path A or path B. It then **preloads(fetch) the instructions** for the predicted path, keeping the pipeline running smoothly. 
  - The last design philosophy for CPU is **instruction versatility(指令多样性/通用性)**. CPUs are built to **understand and execute a large set of instructions**, making them ideal for running **general-purpose software** such as web browsers, office applications, and even video games (though not for the intensive graphics processing needed in some games).  
    - 用途通用，可用指令概括范围广
- **GPU**
  - The primary design philosophy for **GPU** is **high** **throughput**(吞吐量). It is optimized for tasks that can be seperated into smaller and independent tasks. GPUs have a significantly **larger number of cores** compared to CPUs, but each core is **less powerful** and desiged for **smaller tasks**. This allows **GPUs** to process a large amount of data sets and complete a large amount of computations **simultaneously.** 
    - **GPUs** are optimized for **SIMD** operations**, where the same instruction is applied to many data elements **at once.
      - **SIMD** stands for **Single Instruction, Multiple Data.** 
        - 一条指令被“广播”给许多数据元素。
        - 因为图像、矩阵、向量这种任务，本来就是“一次处理很多一样的计算”。
        - GPU 同时让大量数据执行同一种运算，因此它们在**并行计算**上特别快。
    - **GPUs** are designed to **move data efficiently between cores and memory**, prioritizing high bandwidth over complex logic components in each core. 
      - GPU 不追求每个 core 的复杂逻辑处理能力，而是依靠高带宽和海量并行单元来实现超高吞吐量。因此它在处理大量、统一、重复的数据计算时远远快于 CPU

#### Usage Scenarios

- **CPU**
  - running operating systems and managing system resources
  - executing general purpose software tasks
  - decoding and handling user input
  - multitasking between different applications 
- **GPU**
  - processing graphics and rendering images and videos for gaming and video editing
  - accelerating scientific algorithms and machine learning model training
  - encoding and decoding video streams
  - cryptocurrency mining



### Core architecture, processing power, memory access, power efficiency



#### Core architecture

- **Instruction set architecture (ISA)** is an element in the core architecture of CPU, which defines the fundemental operations a CPU can perform.
  - Each instruction in **ISA** specifies a particular operation involving arithmetic operations, data movement, logical operations, control flow changes, or system interactions. 
  - Unique to a CPU are specific **types of instructions** such as **system management instructions** and **complex branching instructions**. 
- **GPU** also has an **ISA instruction set architecture**
  - Each instruction in GPU's ISA is designed for handling extensive arithmetic operations and data movement, and there is less emphasis on complex logical operations and control flow changes. 
  - Unigue to a GPU's ISA are specific types of instructions **optimized for graphics rendering and parallel data processing tasks**, such as the following:
    - **Single instruction, multiple data(SIMD)**: Allow a single operation to be applied simultaneously to a parallel nature of graphics processing and certain types of computational tasks in scientific computing and deep learning.
    - **Texture mapping and manipulation instructions**: Essential for graphics processing, these instructions handle tasks like **pixel interpolation(像素差值 算出中间值的颜色)**and **texture fetching(从纹理图片里拿出某个位置的像素)**, which are important for rendering images and videos. 



####  Processing Power

> refers to the abiilty of a device to perform computational tasks. It is a measure of how much work a CPU or GPU can perform in a given amount of time, which directly impacts the performance of software applications running on these processors.

Factors that may influence the processing power(how much work can be performed in a given amount of time) of CPU and GPU:

- the number of cores: core越多，processing power越大，给定时间能能完成的工作越多
- clock speed: 每秒能“跳动”多少次，是一种频率，指每秒能够完成的clock cycle的数量。时钟越快 → 单核心处理速度越快 → 任务完成得更快
- thermal management: 散热越好 → 处理器越能维持最高性能运行
- power delivery to the processor: 更强的供电 → 芯片能维持高频 + 全核心(core)工作 → 性能(performance)最大化



**CPU:**

- Fewer but more **powerful** cores.
- **High clock speeds** + **high instructions per cycle (IPC)** + **branch prediction** and **out-of-order** execution optimize **sequential task processing**.
- Multithreading allows efficient handling of **multiple task**s and complex computational instructions.

**GPU:**

- Hundreds to thousands of cores, optimized for l**arge-scale parallel processing.**
- High **memory bandwidth** and **specialized** cores (e.g., tensor cores) enhance f**ast processing of large data blocks.**
- **SIMD** allows performing the **same operation on multiple data points** simultaneously, maximizing **throughput**.
- Individual GPU cores may be **lower clocked and simpler**, but are specialized for **parallel execution**, providing **tremendous parallel processing power.**



#### Memory Access

> refers to how these processors retrieve and manipulate data stored in computer memory. 

**CPU:**

- Uses a **memory hierarchy** to efficiently manage data access, typically including L1, L2, and sometimes L3 caches(SRAM).
- This hierarchy is designed to **minimize memory latency** (the delay between issuing a request and receiving the data).
  - This is the advantage of SRAM(cache). CPU get fetch the data/instruction that is being used frequently within a short time period. 
- In multi-core CPU environments, **cache coherence protocols(缓存一致性协议)** are needed to ensure that all cores see a consistent view of memory, preventing data conflicts and maintaining data integrity.

**GPU:**

- Often uses a **unified memory architecture（内存统一架构）**,  allowing both CPU and GPU to access a large shared memory pool.
- Equipped with **high-bandwidth memory** to handle the demands of massive parallel processing. 
- GPUs prioritize **memory throughput(高吞吐量)** over low latency because they need to **feed hundreds to thousands of parallel cores simultaneously**.

**Summary/Comparison:**

- **CPUs** use low-latency memory → optimized for rapid task switching and quick data retrieval/processing.
- **GPUs** use high-throughput memory → optimized for handling large volumes of data and supporting massive parallel computation.



#### Power Efficiency

> CPUs and GPUs use electrical power to perform computational tasks. Power efficiency is a significant aspect of processor design and operation, especially in environments where energy consumption impacts cost, thermal management, and system longevity. 
>
> Power efficiency is often measured **by the amount of computational work performed per watt**.

**CPU:**

- Power efficiency is often measured **by the amount of computational work performed per watt**. This ratio indicates the relationship between **computational output and power consumption** and serves as a benchmark to **compare the efficiency of different CPU models**. Higher performance per watt → more power-efficient CPU. 
- Modern CPUs incorporate advanced power management technologies that adjust power usage based on workload. For example, **Dynamic Voltage and Frequency Scaling (DVFS) 频率调整** reduces power consumption when full processing power is not needed.
- **Thermal Design Power (TDP)** **热设计功耗** is the maximum amount of heat a CPU can generate under normal conditions that the cooling system is designed to dissipate. Efficient CPUs can deliver higher performance while staying within a lower TDP.  指CPU在正常条件下，散热系统能设计处理的最大热量。高效 CPU 能在较低 TDP 下提供更多性能(perfomance)。

**GPU:**

- High-performance computing and gaming GPUs also **emphasize power efficiency** due to **potentially high energy consumption**.
- When handling large workloads, GPUs improve power efficiency by **distributing tasks across many cores**, reducing **power per task compared to serial processing.** 由于总输入功率watt不变，分配到多个cores可以通过parallel computing完成更多的tasks，power efficiency增加，和sequential computing相比。 
- GPUs also have energy-saving features similar to CPUs, such as lowering clock speeds or powering down idle cores.
- GPUs are generally more power-efficient than CPUs for parallel processing tasks.

**Summary/Comparison:** 

- **CPU:** Power efficiency measured as computing work per watt → uses techniques like dynamic voltage and frequency scaling (DVFS) and manages TDP to balance performance and energy use.

- **GPU:** Power efficiency achieved by distributing workload across many cores and parallel processing → can lower clock speeds or close idle cores when full power is not needed.

- **Key difference:** CPUs optimize energy use for variable workloads; GPUs optimize energy use for massive parallel tasks.



### CPUs and GPUs working together: Task division, data sharing, and coordinating execution

> CPUs are designed for general-purpose processing, and GPUs are designed for parallel processing capability. General-purpose processing is executing a variety of instructions with complex logic and decision-making. Parallel processing is performing the same operation simultaneously on multiple pieces of data.

#### Task Division

- **CPU:** Handles sequential and control-intensive tasks → manages the system, performs logic and decision-making, and processes tasks like OS management, network communication, and I/O handling.

- **GPU:** Handles parallelizable, data-intensive tasks → executes hundreds to thousands of independent tasks simultaneously, such as matrix multiplications in machine learning, pixel processing in graphics rendering, and data analysis in scientific computations.

- **Summary:** CPUs coordinate and make decisions, while GPUs perform large-scale parallel computations.



#### Data Sharing

- **Challenge:** For **efficien**t CPU-GPU collaboration, data **must be shared** → initially in CPU memory → t**ransferred to GPU via PCIe(Peripheral Component Interconnect Express,外设互联快线）** which can be a bottleneck.
- **Solution:** **Unified memory(内存统一)** allows CPU and GPU to access the **same physical memory**, simplifying **data sharing and reducing transfer overhead.**

**Summary:** Data sharing is essential for CPU-GPU cooperation, and unified memory minimizes transfer bottlenecks.



#### Coordinating Execution

> Coordinating CPU–GPU execution requires programming models such as CUDA and OpenCL, which handle task division, memory management, and synchronization. Modern systems dynamically choose whether the CPU or GPU handles a task based on workload for optimal performance and energy efficiency.

Modern systems dynamically choose whether the CPU or GPU handles a task based on workload for optimal performance and energy efficiency.

- **屏障（barrier）用于让所有参与线程在继续执行前都到达同一个点。**在并行编程中，屏障用于实现同步点：线程会暂停执行，直到所有参与线程都到达屏障点。最后一个线程到达后，所有线程才会继续后续操作。一种同步机制。
  A *barrier* forces all participating threads(线程) to reach a specific execution point before any can proceed. In parallel programming, barrier is used for implementing synchonization point. The threads will be paused temporarily, until all participating threads reach a specific execution point(barrier point), the threads will run again. A type of synchronization mechanism.

- **事件（event）允许线程等待特定条件发生，并在条件满足时通知一个或多个线程，比屏障更灵活。允许线程在特定条件满足之前等待。与屏障不同，屏障是在预定点同步一组线程，而事件更灵活，可以用来通知一个或多个等待线程，某个特定条件已经发生，例如任务完成或所需数据可用。**一种同步原语。
  An *event* lets threads wait for certain conditions and signals one or more threads when a task is finished or data becomes available, offering more flexibility than barriers. It allows threads wait(pause) until certain conditions are reached. A type of syncrhonization primitive. 



## A1.1.4 Explain the purposes of different types of primary memory



### Registers, cache (L1, L2, L3), random-access memory (RAM), and read-only memory (ROM)



#### Registers

- The **fastest and smallest type of memory**, built **directly** **into the CPU**. They store **data, instructions and addresses** the CPU is **actively executing**. This memory is **volatile ( Requires power to maintain the stored data)**. The fundamental unit of data handled by a CPUs architecture is the word size, which describes the size of a register. In general, registers hold 32 or 64 bits of data.



#### Cache(L1,L2,L3)

- **High-speed** memory residing **on or close** to the CPU. Caches bridge the **speed gap between registers and RAM**, holding frequently used data and instructions for quick retrieval. This memory is volatile(requires power to maintain). 
  - Cache的作用是，和CPU相比，memory的速度太慢了。所以CPU会有空窗期，而cache存frequently used data and instructions，用于加速这个过程(quick retrieval).
  - |1 cache typically ranges from **32 KB to 256 KB per core**, with data and instruction caches separate in some architectures.  一个core一个
  - |2 cache typically ranges from **256 KB to 16 MB per core** or **shared across multiple cores**.  一个core一个或者多个core share
  - |3 cache typically ranges from **2 MB to 32 MB shared across all cores in a CPU.** 多个core share



#### Random Access Memory (RAM)

- The **primary workspace of the computer**. RAM **temporarily ( volatile )** stores the currently running **operating system, processes, and active data and instructions**. This memory is volatile.
  - **SRAM**
    - Cache
    - Fast, stable, won't refresh
    - expensive, less storage place and large volume
  - **DRAM**
    - refresh 不断刷新
    - slow
    - Large capacity, cheaper compare to SRAM



#### Read-only Memory (ROM)

- A **non-volatile** memory that stores **essential instructions and data** for the computer to **start up** (for example, the BIOS or firmware（固件）). 
- The data stored in ROM is only modifiable through special processes. 
- ROM's role is primarily for **firmware storage** and it is not directly involved in the day-to-day memory access hierarchy involving registers, cache and RAM. ltis better considered as a **separate entity focused on system boot-up（启动） and low-level startup operations.** Used primarily for starting up a computer. 



### The interaction of the CPU with different types of memory to optimize performance

> The interaction between CPU and memories is guided by the principles of minimizing latency and maximizing throughput for data and instruction access.
>
> - Latency:  is the time it takes for data to move from its source to its destination. Latency is usually described as low or high.

- Throughput: is the amount of data that can be processed or transmitted in a given amount of time.



#### Interaction between CPU and Registers

- **Direct Interaction**:  The CPU has **internal registers**, which are the fastest type of memory available. These registers are used to store **immediate data** which the CPU **needs for current operations**, such as **operands for arithmetic operations, address pointers, and the results of operations.** 

- **Optimization**: By utilizing registers for the **most immediately necessary data and instructions**, the CPU minimizes the **need** to **access slower types of memory,** significantly speeding up processing times. 



#### Interaction between CPU and Cache(L1, L2, L3)

- **Hierarchical use**: Cache memory serves as a high-speed intermediary between the CPU and the slower main memory (RAM). 
  - L1 has the smallest capacity but fastest speed. L3 has the largest capacity but slowest speed, but **stiil faster than RAM.**
- **Data and instruction prefetching**: Modern CPUs use **advanced prediction algorithms** to anticipate which data and instructions **will be needed soon**, and **load them into the cache** ahead of time（提前）. This reduces data-waiting delays and improves overall performance.
- **Spatial and temporal locality 时间空间局部性**: Caches use spatial locality (nearby data is likely to be accessed soon) and temporal locality (recently accessed data will likely be reused) to keep relevant information close to the CPU, improving performance.



#### Interaction between CPU and Main Memory (RAM)

- **Central Data Repository**: RAM holds the **operating system**, **applications** and **data** that are currently in use. It provides a much larger space for data storage compared to caches and registers. 
- **Interaction through momory controller**: The CPU accesses RAM **through the memory controller**, which manages **data transfers, controls access timing, and optimizes the data flow** between them. In order to improve the performance. 
- **Virtual Memory (虚拟内存)**: Virtual memory uses **part of the hard drive or SSD** to extend system memory. The CPU swaps data between RAM and this virtual space, but accessing it is **much slower** than using RAM directly. 



#### Interaction between CPU and the Read-only memory (ROM)

- **Boot-up (start up) process**: ROM stores the **firmware or BIOS** used during **computer startup**. The CPU reads this data at boot(启动时) to initialize hardware and load the operating system from secondary storage into RAM.

  

### The relevance of terms cache miss and cache hit

- In order to fetch the data/instruction, The CPU checks **registers** first, then **L1, L2, L3 caches**, and **finally RAM** to find needed data. If the data is found in a cache (**a cache hit**), access is **very fast**. If it’s not found (**a cache miss**), the CPU must **fetch it from RAM, which is slower.**
- To **reduce** cache misses, CPUs use techniques such as **prefetching** (**predicting and loading needed data to cache early**), **smart memory allocation (placing data to improve hit rates)**, and **cache replacement policies (deciding which data to remove when the cache is full)**.



 



## A1.1.5 Describe the fetch, decode and execute cycle

> The fetch-decode-execute cycle is the fundamental cycle of instruction execution in a computer. This cycle is also known as the instruction cycle. 

- **Fetch** : the CPU fetches an instruction from your memory(`RAM`).  
- **Decode**: The CPU decodes the instruction, which means it interprets the instruction into a set of low level operations that the CPU can execute. 
- **Execute**: The CPU executes the instruction, which means it carries out the low level operations that were specified in the decoded instruction. 



### The **Fetch** Phase

In the **fetch** phase, **the CPU retrieves a machine language instruction from main memory(often `RAM`). It involves the CPU sending a request to `RAM` to fetch the instruction.** The address of the instruction is then being strored in `MAR`, and the fetched instruction is then transferred to a special register called the `IR` in register. 

The complete process is like this:

1. **Address Identification:** The address of the next instruction, held in the **Program Counter (PC)** (often assumed but crucial), is transferred to the **Memory Address Register (MAR)**. This happens internally within the CPU.
2. **Address Transmission:** The address in the **MAR** is then placed onto the **Address Bus**. The **Address Bus** is **unidirectional**(单向的), carrying the memory location from the CPU to the **RAM**.
3. **Command Issuance:** Simultaneously, the **Control Unit (CU)** asserts a $\text{READ}$ signal onto the **Control Bus**. The **Control Bus** carries the command necessary to execute the operation.
4. **Data Retrieval:** **RAM** receives the address (via the **Address Bus**) and the $\text{READ}$ command (via the **Control Bus**). It locates the instruction and places its binary contents onto the **Data Bus**(instructions or data are all knowns as data).
5. **Data Reception:** The instruction travels across the **Data Bus** (which is **bidirectional**) and is temporarily held in the **Memory Data Register (MDR)** within the CPU. So you get the idea that **MDR** holds the intruction or data that is being transferred from or to memory. 
6. **Instruction Loading:** Finally, the instruction is transferred from the **MDR** to the **Instruction Register (IR)**, where it will be held for the remainder of the cycle. Here you also get the idea that **IR** holds the current instruction being executed. 
7. **Preparation:** The **PC** is incremented to point to the subsequent instruction address. Most times **PC** is incremented automatically.

### The **Decode** Phase

In **decode** phase, the CPU interprets the machine language instruction fetched during the previous phase. This phase is primarily done by the **CU (control unit)**, which decodes the instruction by analyzing these possible components:

- **Opcode (operation code)**: dictates(规定) the type of operation
- **Operands**: The data/address to be operated on
- **Addressing Modes**: Determine how to load the **operands**

The complete process is like this:

- The goal of the Decode Phase is for the **Control Unit** to interpret the instruction held in the **IR** and determine the necessary steps for execution.

1. **Instruction Analysis:** The **CU** examines the instruction in the **IR**. It parses the **Opcode** (what operation to perform, e.g., $\text{ADD, STORE}$) and the **Operand** (the data or address to operate on).
2. **Control Signal Preparation:** Based on the decoded instruction, the **CU** generates the precise sequence of micro-operations (control signals) required for the Execution Phase. These signals will be transmitted across the **Control Bus**.
3. **Address Staging:** If the instruction requires data from **RAM** (e.g., $\text{ADD}$) or needs to store data back to **RAM** (e.g., $\text{STORE}$), the memory address (the Operand) is immediately extracted from the **IR** and placed into the **MAR**. This is an internal CPU operation preparing for the bus usage in the next phase. The **ACC** remains static during this phase.

### The **Execute** Phase

During the **execute** phase, the CPU performs the operations specified by the instruction decoded in the previous phase. The specific operation carried out is dictated by the opcode. Common operations include the following:

- **Arithmetic Operations:** Addition, Substraction, Multiplication, Division. These operations are often done by the **ALU**.
- **Logical Operations**: Logical functions like ${\text{AND}}$, ${\text{OR}}$ and ${\text{NOT}}$, also managed by the **ALU**. 
- **Memory Access Operations**: Load(reading data from memory into register) and store(writing data from register to memory). These involve operations with the memory. 
- **Control operations**: Conditional and unconditional jumps which alter the flow of execution based on specific conditions. 

The complete process is like this:

- This is the action phase, where the **CU** coordinates/activates the components to perform the task specified by the instruction. The operations heavily depend on the instruction type:
- A. **Data Transfer to/from RAM** (e.g., $\text{LOAD}$ or $\text{STORE}$)
  - The **MAR** sends the data address onto the **Address Bus**.
  - The **CU** asserts a $\text{READ}$ or $\text{WRITE}$ command via the **Control Bus**.
  - For $\text{LOAD}$ (reading data), data travels from **RAM** $\to$ **Data Bus** $\to$ **MDR** $\to$ **ACC**.
  - For $\text{STORE}$ (writing data), data travels from **ACC** $\to$ **MDR**; then, **MDR** $\to$ **Data Bus** $\to$ **RAM**.
- B. **Arithmetic/Logic Operations** (e.g., $\text{ADD}$ or $\text{AND}$)
  - Data sources (often the **ACC** and the **MDR**—containing data fetched from RAM using the bus system) are supplied to the **Arithmetic Logic Unit (ALU)**. This transmission occurs on the internal CPU bus.
  - The **CU** sends the specific operation command (e.g., $\text{ADD}$) to the **ALU** via the **Control Bus**.
  - The **ALU** performs the calculation.
  - The result is written back to the **ACC**, ready for the next operation.
- **Cycle Completion**
  - Once the instruction is executed, the **Control Unit** signals the end of the current cycle. The CPU immediately loops back to the **Fetch Phase**, using the updated address in the **PC** to begin retrieving the next instruction.   

### Examples of the **FDE Cycle**

#### (1) CPU Processing Cycle: WRITE Value 0x7E to Address 0x4F2

This outlines the Fetch-Decode-Execute Cycle for an instruction to write the value $\text{0x7E}$ to memory location $\text{0x4F2}$.

**Initial State Assumptions:**

* **PC:** $\text{0x100}$
* **ACC:** $\text{0x7E}$
* **Instruction:** $\text{STA 0x4F2}$ (Store Accumulator to $\text{0x4F2}$)

#### 1. 🚶 FETCH Phase: Getting the Instruction

1.  The address of the next instruction is moved: $[\text{PC}]$ ($\text{0x100}$) $\to \text{MAR}$ (Internal CPU Bus).
2.  The $\text{PC}$ is incremented: $[\text{PC}] + 1 \to \text{PC}$ ($\text{0x101}$).
3.  The address is placed on the bus: $[\text{MAR}] \to$ **Address Bus**.
4.  The $\text{CU}$ commands the read: $\text{CU}$ sends $\text{READ}$ signal $\to$ **Control Bus**.
5.  The instruction is retrieved: $\text{RAM[0x100]} \to$ **Data Bus** $\to \text{MDR}$.
6.  The instruction is loaded: $[\text{MDR}] \to \text{IR}$ (Internal CPU Bus).

#### 2. 🧐 DECODE Phase: Setting Up the Write

1.  The $\text{CU}$ decodes the instruction ($\text{STA}$) from the $\text{IR}$ and identifies it as a $\text{WRITE}$ operation.
2.  The destination address is staged: $[\text{IR}_{Operand}]$ ($\text{0x4F2}$) $\to \text{MAR}$.
3.  The data to be written is staged: $[\text{ACC}]$ ($\text{0x7E}$) $\to \text{MDR}$.

#### 3. ⚙️ EXECUTE Phase: Writing to Memory  

1.  The destination address is stabilized: $[\text{MAR}]$ ($\text{0x4F2}$) $\to$ **Address Bus**.
2.  The $\text{CU}$ commands the write: $\text{CU}$ sends $\text{WRITE}$ signal $\to$ **Control Bus**.
3.  The data is transmitted: $[\text{MDR}]$ ($\text{0x7E}$) $\to$ **Data Bus**.
4.  $\text{RAM}$ receives the address, command, and data.
5.  The data stored on that memory location is updated: $\text{RAM[0x4F2]}$ is set to $\text{0x7E}$.

#### 🔄 Cycle Complete

* The **Control Unit** signals the end of the current cycle.
* The $\text{CPU}$ loops back to the $\text{FETCH}$ phase, using the updated $[\text{PC}]$ ($\text{0x101}$) to begin the next instruction.

#### (2) CPU Processing Cycle for Comparison Instruction: $\text{CMP R1, R2}$

**Instruction Meaning:** Compare the value in register $\text{R1}$ with the value in register $\text{R2}$. The result of the comparison is used only to set the CPU Status Flags (e.g., Zero Flag, Carry Flag); no register receives the output.

**Initial State Assumptions:**

* **PC:** $\text{0x300}$ (Address of $\text{CMP}$ instruction)
* **R1:** $15$
* **R2:** $10$
* **Flags:** All flags are initially cleared.

#### 1. 🚶 FETCH Phase: Getting the Instruction

1.  The address is prepared: $[\text{PC}]$ ($\text{0x300}$) $\to \text{MAR}$ (Internal CPU Bus).
2.  The $\text{PC}$ is incremented: $[\text{PC}] + 1 \to \text{PC}$ ($\text{0x301}$).
3.  The address is transmitted: $[\text{MAR}] \to$ **Address Bus**.
4.  The $\text{CU}$ commands the read: $\text{CU}$ sends $\text{READ}$ signal $\to$ **Control Bus**.
5.  The instruction is retrieved: $\text{RAM[0x300]} \to$ **Data Bus** $\to \text{MDR}$.
6.  The instruction is loaded: $[\text{MDR}] \to \text{IR}$ ($\text{CMP R1, R2}$ is now in $\text{IR}$).

#### 2. 🧐 DECODE Phase: Interpreting the Comparison

1.  The $\text{CU}$ decodes the instruction ($\text{CMP}$) from the $\text{IR}$. 
2.  The $\text{CU}$ identifies the instruction as an $\text{ALU}$ operation that requires the contents of $\text{R1}$ and $\text{R2}$.
3.  The $\text{CU}$ prepares the sequence of signals to use the $\text{ALU}$ for subtraction while directing the result **not** to be stored in a register like the $\text{ACC}$.

#### 3. ⚙️ EXECUTE Phase: Performing the Comparison

1.  **Preparation for Subtraction:** $[\text{R1}]$ ($15$) and $[\text{R2}]$ ($10$) are moved to the inputs of the $\text{ALU}$ (Internal CPU Bus). *Note: Comparison is typically performed by subtraction: $\text{R1} - \text{R2}$.*
2.  **ALU Operation:** The $\text{CU}$ sends the $\text{SUBTRACT}$ command to the $\text{ALU}$ (via the **Control Bus**).
3.  **Result and Flags:** The $\text{ALU}$ calculates the difference ($15 - 10 = 5$).
    * The arithmetic result ($5$) is **discarded** (it does not load into $\text{R1}$ or $\text{ACC}$).
    * **Crucially, the resulting condition** is used by the $\text{ALU}$ to set the **CPU Status Flags**.
4.  **Flag Setting:** Since the result (5) is positive and non-zero:
    * The **Zero Flag** is cleared (set to 0).
    * The **Carry Flag** (Borrow) is cleared (set to 0, assuming unsigned arithmetic).
    * The **Sign/Negative Flag** is cleared (set to 0).
5.  **Control Flow Enablement:** The setting of these flags now enables future conditional instructions (like $\text{BGT}$, $\text{BLE}$, etc.) to alter the $\text{PC}$ based on this comparison.

#### 🔄 Cycle Complete

* The $\text{Control Unit}$ signals the cycle end.
* The $\text{CPU}$ begins the next $\text{FETCH}$ phase from the updated $[\text{PC}]$ ($\text{0x301}$).



## A1.1.7 Describe internal and external types of secondary memory storage

> Secondary memory storage is non-volatile and retains data even when the computer is powered off, enabling data persistence. Examples of secondary memory storage include hard disk drives (HDDs), solid-state drives (SSDs), optical discs, and flash drives. 



### Internal hard drives (SSD, HDD) and embedded multimedia cards (eMMCs)



#### Internal hard disk drives (HDDs)

- A type of storage device that stores data on magnetic disk platters. 

- HDDs are the most common type of **internal storage**, and they are typically used in desktop computers, laptops and servers.
- HDDs offer **high storage capacities and are very reliable**, but they can be **comparatively slow to access data** (average sustained data transfer rate for a hard disk is between **100 MB/s to 200 MB/s**). 
- A hard disk drive (HDD) is called **“hard”** because it uses **rigid, non-flexible magnetic platters（磁盘）**to store data, unlike the bendable floppy disks used in the past. 
  - Inside an HDD, several **platters** **spin at high speed** while a **read/write** **head(读写磁头)** moves across **their surfaces**. The head **stores and retrieves data by magnetizing tiny regions on the platter, almost like writing on a fast-spinning metal disc.** 读写头通过**磁化盘面上的微小区域**来记录或读取数据，就像在一张飞速旋转的金属唱片上“刻字”和“读字”。
- Advantages of HDD:
  - Large store capacities
  - high reliability
  - relative affordability, compared to SSD
- Disadvantages of HDD:
  - slow data access speeds
  - noisy during working
  - may be damaged from drops or shocks because of moving parts
  - higher power consumption: requires more energy to spin the magnetic platters

---

#### Solid-State Drives (SSDs)

- Another storage device that uses **non-volatile flash memory** to store data, offering **much faster access speeds, lower power consumption, and greater durability** than traditional hard disk drives because it **contains no moving parts(no spinning magnetic disk platters).** 

- SSDs serve the same purpose as traditional hard disk drives (HDDs) but are **faster and consume less power.** SSDs have no moving parts, leading to **quicker access times and lower latency.**

- The average data transfer rate for an SSD can **significantly exceed that of HDDs**, in some cases reaching **2,500 MB/s to 7,000 MB/s.** 

- How it works?

  - An SSD stores data using **NAND flash memory**, a **non-volatile** technology that retains information without power. Data is kept in **floating-gate transistors (memory cells) 浮栅晶体管** arranged in a grid. Each cell stores a bit (or multiple bits) by **holding or releasing electrical charge.**
  - NAND flash is structured into **blocks**, which contain smaller **pages**. Data is **written in pages** but **erased in entire blocks**. Reading involves **sensing the charge level in the floating gate transistor.**
  - An internal **SSD controller** handles key tasks such as **data transfer, error correction, and wear-levelling（磨损均衡）**—an algorithm that spreads **write/erase cycles** evenly to **extend lifespan**, since flash cells endure only limited write cycles.
  - NAND flash types include **SLC, MLC, TLC, and QLC**, storing 1, 2, 3, or 4 bits per cell respectively, each balancing cost, speed, and endurance differently.
    - **Memory cell** 是最小单位,
    - 每个 memory cell 是一个 **floating-gate transistor**，
    - 无数 cells 排成一个 **grid**，
    - **Grid** 是由所有 memory cells 组成的物理网格结构，**Page** 是从该网格中划分出来、用于写入和读取操作的逻辑单元，
    - 这些 **cells** 被组织成一个个 **pages（最小写入单位）**，
    - 多个 **pages** 再组成 **blocks（最小擦除单位）**。

- The sophisticated R/W/E cycle of SSD:

  - Each memory cell is a tiny transistor. It contains a **floating gate** in the middle. The floating gate can **trap or release electrical charge**.
  - **Writing** 
    - When writing a 1 or 0, the SSD controller **applies voltage to inject or remove charge** in the floating gate. The charge state determines the cell’s **binary value** (or multiple bits for multi-level cells).
  - **Reading**
    - Data is read by **sensing the charge** in the floating gate to determine whether the cell stores 0 or 1.
  - **Erase**
    - The floating gates of all cells in a **block** are cleared simultaneously. Therefore, **erase operations are performed per block**, while **write operations are performed per page**.

  

- Advantages of SSD: 
  - **fast** access speed
  - **high** data transfer rate
  - **Low** power usage(no spinning magnetic disk platters)
  - **strong durability** due to the absence of mechanical parts
  -  No spinning disks or moving heads, so **operation is quiet**
- Disadvantages of SSD:
  - **higher** cost per gigabyte
  - **Limited write/erase cycles:** NAND flash cells can only endure a **finite** number of writes/erases before wearing out(磨损）
  - **Capacity limitations:** The average capacity a SSD can reach is **much smaller** than HDD

---

#### Embedded multimedia cards (eMMCs)

- eMMC is a **type of NAND flash memory storage** that integrates the memory, controller, and multimedia card interface in a **single package on a device's motherboard.**

- **Characteristics:**

  - Solid-state, but **generally slowe**r than SSDs (lower sequential read/write speeds and IOPS)

  - Storage capacity typically **16–256 GB**

  - **Lower cost** than SSDs, commonly used in budget devices

- **Advantages:**

  - Fast data access

  - Reliable and shock-resistant

  - Affordable for **low to mid-range devices**

- **Disadvantages:**

  - Slower than SSDs

  - Limited storage capacity compared to SSDs and HDDs

  - More expensive than HDDs

---

### External hard drives, optical drives, flash drives, memory cards, and network attached storage



#### External hard drives(SSD, HDD)

- come in a variety of sizes and capacities, and they can be used to back up important data, transfer files between computers, or simply store data. The basic functionality of external HDDs and SSDs is the same as for internal HDDs and SSDs. 

---

#### Optical Drives

- An optical drive reads and writes data **on optical discs using laser technology**
- Storage Mechanism:
  - Data is stored as **pits（凹点）and lands（平地)** on a **spiral track (螺旋轨道**) of a polycarbonate disc with a reflective metal layer. 
- Read Process:
  - Laser light reflects **differently off pits and lands**; sensors detect light variations and convert them to electrical signals. 
- Advantages:
  - High storage capacity, compatible with older devices. 
- Disadvantages:
  - Slower data access, fragile, easily scratched or dusty. 

---

#### Flash Drives/USB Flash Drives

- Small, portable storage devices that connect via USB.
- Uses NAND flash memory to store data.
- Portable, fast data transfer, relatively affordable.
- Lower storage capacity than HDDs/SSDs; data loss possible; losing the device may cause security risks.

---

#### Memory Cards 存储卡

- Memory cards are **small, removable storage devices** that are typically used in portable devices, such as **smartphones, tablets and digital cameras.** 
- Uses NAND flash memory to store data.
- Portable, compact（体积小巧）, available in various capacities.
- Easily lost or damaged; may not be compatible(兼容) with all devices.

---

#### Network attached storage 

- **Centralized** storage device accessible by **multiple devices on a network.**
- Uses HDDs, SSDs, or hybrid combinations(混合使用); can be configured with RAID
  - RAID（Redundant Array of Independent Disks 独立磁盘冗余阵列）把多块硬盘组合在一起，来防止硬盘故障并保证数据可用性
- Centralized storage, shared access for multiple devices, scalable, high administrative control.
- More expensive than individual external drives, requires configuration, requires network connection.



## A1.1.8 Describe the concept of compression

> Compression can significantly decrease the amount of disk space needed for files and the bandwidth required for transferring them, facilitating more efficient use of resources. 



### Lossless and Lossy Compression Methods

---



#### Lossless Compression

- Lossless compression **identifies redundant patterns** and **eliminates them** without losing any essential information. 
- This ensures that the **decompressed(解压缩 从压缩状态恢复到原文件状态) file** is an exact **replica** of the original file, preserving its **integrity and quality.** The process of lossless compression is reversible, without losing any essential information.
- The compression ratio achieved through lossless compression is generally smaller comparing lossy compression.

---

#### Lossy Compression

- Lossy compression employs a more **aggressive strategy** to achieve higher compression ratios. 
- It **deliberately discards some data**, typically **minor details** that are **less noticeable (perceptual redundancy)** to the human eye or ear. 
- This allows for **significantly smaller file sizes**, making it suitable for applications such as **audio, video and images.** However, the discarded information can **compromise（危及 损害）the quality of the reconstructed file.**  This means that this process is irreversible.
- Lossy Compression achieves higher compression ratio(smaller file size) but deliberately omitting some details.

---

### Differences between lossless and lossy compression

| Feature                    | Lossless Compression                                         | Lossy Compression                                            |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Data Integrity             | Preserves **all original data**; the decompressed file is identical to the original. | Introduces variations because **some data is deliberately discarded** as less critical. |
| Compression Ratio          | Lower compression ratios since **no data is removed.**       | Higher compression ratios achieved by **removing less important data**. |
| Applications               | Used when data integrity is **critical**, e.g., backups, archives, and document editing. | Used for audio, video, and images where **slight quality loss** is acceptable for smaller file sizes. |
| Perceptual Redundancy      | Does not exploit perceptual redundancy.                      | Exploits perceptual redundancy, **discarding details humans are unlikely to notice.** |
| Reversible vs Irreversible | Reversible — original data can be **perfectly reconstructed(decompressed).** | Irreversible — discarded data **cannot be restored**, causing **permanent information loss.** |

---



### Run-length encoding, transform coding 



- **Run-length encoding(RLE)** is a simple and efficient **lossless compression technique** that is well suited for data with **repetitive patterns**. It works by **identifying and replacing consecutive occurrences** **of the same value** with a single code that represents the **length of the run**. For instance, the sequence AAAAA would be encoded（编码）as 5A. 

- **Transform coding**, on the other hand, is a more advanced **lossy** **compression technique**. It uses mathematical transformations (like the DCT(discrete cosine transform)) to convert data into a form where **its structure and redundancy are easier to identify**. This makes it far more efficient for complex data and enables much higher compression ratios.

  - Transform coding is a technique of lossy compression, because the compressed file cannot be perfectly reconstructed. The process is irreversible, where some data and information are being deliberately discarded permanently. 

  It is widely used in:

  - **JPEG**, which transforms images into **frequency domain representation before quantizing(量化）**

  - **MP3**, which transforms audio signals into **frequency domain representation before encoding(编码)** 

    

| Compression Type     | Examples                          | Typical Applications                                        |
| -------------------- | --------------------------------- | ----------------------------------------------------------- |
| Lossless             | GIF, TIFF, PNG, PDF, ZIP          | Backups, archives, text files, simple graphics              |
| Lossy                | JPEG, MP3, MP4                    | Images, audio, video where small quality loss is acceptable |
| Technique (Lossless) | Run-Length Encoding (RLE)         | Fax images（传真）, simple graphics, text compression       |
| Technique (Lossy)    | Transform Coding (JPEG, MP3, MP4) | Images, audio, video compression                            |








## A1.1.9 Describe the different types of services in cloud computing

> The term "cloud" refers to cloud computing, where organization are allowed to access and utilize computing resources (such as servers, storage, databases) over the internet to offer flexible resources.
>
> Organizations can save money by only paying for the **computational resources they use**, rather than paying for **an expensive server** which they **might not use at full capacity all the time.** 



### Software as a service(SaaS)

- **SaaS** is a cloud computing model where **software applications are hosted and managed** by a third-party provider and accessed by organizations **through a web browser or mobile app over the internet.** **SaaS** eliminates the need for organizations to **install and maintain software on their own devices**, making it convenient and cost-effective. 
- Software as a service的service指的是软件不用下载、不用安装、不用自己维护，直接在网上用就行。

Key Characteristics of software as a service(SaaS):

- **All-inclusive**: Organizations have access to the full application suite with automatic updates and maintenance, without any upfront costs.

- **Scalability**: SaaS applications can be easily **scaled up or down** to meet changing organizational needs, ensuring optimal performance and resource utilization. 

- **Accessiblity**: SaaS applications are **accessible** from anywhere **with an internet connection**, providing organizations with **flexibility and mobility.** 

- **Security**:  SaaS providers implement **robust security measures** to protect **sensitive organizational data** and **ensure the integrity of the applications.**

- Examples of **SaaS**:

  - Gmail

  - Canva

  - Google Sheets

  - Google Docs

  - Google Drive

    


---



### Platform as a service(PaaS)

- **PaaS** provides a **cloud-based** environment(**on the internet**) for developers to build, deploy, and manage their applications.

Key Characteristics of PaaS: 

- **DevOps-friendly:** PaaS supports **rapid development and deployment cycles**. DevOps is a set of practices which **combines software engineering (Dev) and information technology (Ops).** 
- **Infrastructure Abstraction**: PaaS simplifies application management by handling **OS updates, database administration, and networking configuration.**
- **Reduced operational costs**: PaaS eliminates the need to **purchase and maintain hardware and software.** 



- **Examples of PaaS Applications**

  - Heroku: A **fully managed platform** where you **deploy apps simply by pushing your code.**

  - Google App Engine: A Google-powered platform that **auto-scales** and **runs your app with minimal configuration.**

  - Firebase: A **backend-in-a-box** that gives you **databases, auth, hosting, and more without managing servers.**

  - Azure App Service: Microsoft’s fully managed environment for **building, deploying, and scaling web apps effortlessly.**

    

---



### Infrastructure as a service (laaS)

- **laaS** provides **virtualized** computing resources, such as **servers, storage and networking, over the internet**. It gives businesses the flexibility to provision and manage t**heir own IT infrastructure** without the need to **invest in physical hardware and software.** 
- **Virtualization** uses software to **create virtual versions of hardware resources**, allowing multiple independent **virtual machines** to run on a single physical device. Each VM behaves like a **separate computer** with its own operating system and applications. This technology improves hardware utilization, enhances flexibility, simplifies management, enables scalability, and provides strong isolation for better security.

**Key Characteristics of IaaS:**

- **Customization**: **IaaS** allows businesses and firms to **tailor(定做) their own IT structures to their specific needs and requirements.** 
- **Scalability**: Resources can be **easily provisioned and scaled up or down** as needed, ensuring optimal perfomance. 
- **Control**: Businesses have **full control** over **configuration and management** of their IaaS infrastructure.



**Examples of IaaS Applications:** 

- Amazon Web Service(AWS): Provides on-demand **virtual servers** where you **control the OS, storage, and network.**
- Microsoft Azure Virtual Machines: Offers **scalable VMs** where you **manage everything above the hardware layer.**
- IBM Cloud Virtual Servers: Provides **secure, flexible VMs** designed for **enterprise-level workloads.**
- Google Compute Engine(GCE): Gives **highly customizable virtual machines** running on Google’s global infrastructure.



---



### Choosing the right cloud service model


| Feature                 | **SaaS**                             | **PaaS**                                     | **IaaS**                                                     |
| ----------------------- | ------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| **Control**             | Lowest                               | Medium                                       | Highest                                                      |
| **Flexibility**         | Lowest                               | Medium                                       | Highest                                                      |
| **Resource Management** | Service provider manages everything  | Service provider manages most resources      | Customer manages most resources(service providers manage the physical resources(eg.physical servers)) |
| **Cost**                | Most cost-effective                  | Medium cost                                  | Most expensive                                               |
| **Suitability**         | Basic applications for general users | Rapid development/deployment and custom apps | Specialized apps with hardware access                        |










