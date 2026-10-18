# شرح شامل للشبكات (Networks) — ملخص المحاضرات الأربع
**Network Fundamentals + OSI + Data Link Layer**

> ملاحظة مهمة قبل ما نبدأ: كل مصطلح إنجليزي مهم هيظهر بالـ **Bold** وسط الشرح عشان تحفظه زي ما هو بالظبط في المتحان.

---

# 🌐 المحاضرة 1: أساسيات الشبكات (Network Fundamentals)

## 1) إيه هي الشبكة أصلاً؟

**Network (شبكة)** = مجموعة من الأجهزة (بتسمى **Nodes**) متوصلة ببعضها عن طريق **Communication Links** (قنوات اتصال)، بحيث تقدر تبعت وتستقبل بيانات من بعض.

**Computer Network** تحديدًا = مجموعة من الكمبيوترات المستقلة (**Autonomous Computers**) متوصلة ببعضها بتقنية واحدة، ويكونوا قادرين على تبادل البيانات.

- الـ **Node** ممكن تكون: كمبيوتر، لابتوب، طابعة، سيرفر، تليفون، كاميرا... أي جهاز يقدر يرسل أو يستقبل.
- الإنترنت هو أشهر مثال على **Network of Networks** (شبكة مكونة من شبكات).

## 2) ليه نستخدم الشبكات؟ (Benefits of Networks)

| الميزة | الشرح |
|---|---|
| **1. Data Exchange** | تبادل البيانات بين جهازين أو أكتر. أمثلة: Email, VoIP, E-commerce |
| **2. Sharing Resources** | مشاركة الهاردوير والسوفتوير: طابعات، تخزين، سيرفرات، تطبيقات، إنترنت |

### نموذج العميل والسيرفر (Client-Server Model)
- **Client** بيبعت **Request** (طلب) ← عبر الشبكة → **Server** بيعالج الطلب ويرد **Response**.

## 3) مهام الشبكة (Network Tasks) — شبكة بتعمل إيه؟

⚠️ **فرق مهم جدًا اسأل عليه:**
- **Network Tasks** = الشبكة **بتعمل إيه** (وظيفة تقنية)
- **Network Benefits** = إحنا **بنكسب إيه** من الشبكة

| # | المهمة | الشرح |
|---|---|---|
| 1 | **Communication** | السماح للأجهزة والمستخدمين بالتواصل وتبادل المعلومات (Data, Email, Voice, Video conferencing) |
| 2 | **Data Transmission** | نقل البيانات من Sender → Network → Receiver |
| 3 | **Addressing** | تحديد هوية الأجهزة ومعرفة مصدر ووجهة البيانات. مثال: **MAC Addresses** و **IP Addresses** |
| 4 | **Routing** | تحديد المسار المناسب للـ **Packets** من المصدر للوجهة |
| 5 | **Switching & Forwarding** | أجهزة زي **Switches** و **Routers** بتوجه البيانات لوجهتها |
| 6 | **Network Management** | مراقبة الشبكة وإعداداتها وصيانتها |
| 7 | **Access Control** | التحكم في مين مسموح له يوصل للموارد والخدمات |
| 8 | **Security** | حماية البيانات من الوصول غير المصرح به. أمثلة: **Authentication, Encryption, Firewalls** |
| 9 | **Error Control & Reliability** | اكتشاف الأخطاء والتعافي منها |
| 10 | **Traffic Management** | إدارة الازدحام. أمثلة: **Traffic Prioritization, QoS, Congestion Control, Traffic Shaping** |

## 4) مكونات الشبكة (Elements of a Network) — 5 عناصر أساسية

| العنصر | التعريف |
|---|---|
| **1. Devices (الأجهزة)** | بتبعت وتستقبل الرسائل (كمبيوتر، تليفون، كاميرا...) |
| **2. Medium (وسط النقل)** | المسار الفيزيائي اللي بتمشي فيه الرسالة من المرسل للمستقبل |
| **3. Message (الرسالة)** | المعلومات المراد توصيلها: نصوص، أرقام، صور، صوت، فيديو |
| **4. Protocol (البروتوكول)** | القواعد اللي بتحكم تدفق الرسائل — اتفاق بين الأجهزة المت communicative. **من غير Protocol الأجهزة متوصلة بس مش بيتكلموا** (زي واحد بيتكلم فرنسي وواحد عربي بس!) |
| **5. Intermediary Devices (أجهزة وسيطة)** | بتربط الـ Hosts بالشبكة وبتوصل شبكات ببعض (Switches, Routers...) |

## 5) وسائط النقل (Transmission Media) — نوعين كبار

```
Transmission Media
├── Guided (Wired) — موجه (سلكي)
│   ├── Twisted Pair (UTP / STP)
│   ├── Coaxial Cable
│   └── Fiber-Optic Cable
└── Unguided (Wireless) — غير موجه (لاسلكي)
    └── Free Space (هواء/فراغ)
```

| النوع | الوصف |
|---|---|
| **Twisted Pair (UTP)** | الأكثر استخدامًا في Ethernet LANs، رخيص وسهل |
| **STP (Shielded)** | نفس الـ Twisted Pair بس بدرع (**Shield**) → مقاومة ضوضاء أعلى |
| **Coaxial Cable** | نحاس في النص + Mesh حواليه → إشارات عالية التردد |
| **Fiber-Optic** | نواة زجاج (**Glass Core + Cladding**) → أعلى سرعة وBandwidth، للمسافات الطويلة |
| **Wireless** | Bluetooth, Wi-Fi, Microwave, Satellite, Infrared, Cellular |

## 6) التعريفات الأساسية للسرعات (مهمة جدًا وبتتلخبط)

| المصطلح | التعريف | يشمل Overhead؟ | نظري ولا حقيقي؟ |
|---|---|---|---|
| **Bit Rate** | عدد الـ Bits اللي بتتنقل في الثانية | Yes | Theoretical |
| **Data Rate** | إجمالي البيانات المرسلة (مفيدة + تحكم) | Yes | Theoretical |
| **Link Rate** | أقصى سرعة نظرية للينك الفيزيائي | Yes | Theoretical |
| **Information Rate** | الـ Bits المفيدة **بس** (من غير Overhead) | **No** | Theoretical |
| **Throughput** | معدل التسليم الفعلي الناجح فعلًا | **No** | **Real (مقاس)** |

### القاعدة الذهبية (احفظها):
```
Throughput ≤ Information Rate ≤ Data Rate ≈ Bit Rate ≤ Link Rate
```

**مثال تطبيقي:** Link Rate = 200Mbps (الحد الأقصى النظري)، Data Rate = 100Mbps، Overhead = 20% → Information Rate = 80Mbps، Throughput = 60Mbps (اللي المستقبل فعلًا بيوصله بعد التأخيرات والتداخل).

## 7) Network Edge vs Network Core

| | **Network Edge (حافة الشبكة)** | **Network Core (قلب/عمود الشبكة)** |
|---|---|---|
| المكان | أقرب جزء للمستخدم النهائي | الجزء المركزي عالي السرعة |
| المكونات | PCs, Laptops, Smartphones, IP phones, IoT, Access Points, Edge Routers | High-speed Routers, Core Switches, High-capacity Links, Redundant connections |
| الوظيفة | توصيل الأجهزة النهائية + إرسال واستقبال الـ User Traffic + تطبيق سياسات الوصول والأمان | نقل البيانات بسرعة وموثوقية بين أجزاء الشبكة المختلفة |
| المميزات | وصول المستخدمين للتطبيقات | Fast forwarding, High availability, High capacity, **Low latency**, Reliability |

> **ببساطة:** Edge = بيوصل المستخدمين بالشبكة ✅ | Core = بينقل الـ Traffic بين الشبكات ✅

---

# 🔀 المحاضرة 2: Switching و Transmission

## 1) تعريفات أولية

- **Transmission (إرسال)**: نقل الإشارة من المصدر للوجهة بحيث جودة الإشارة عند المستقبل تلبي معايير أداء معينة.
- **Switching (تبديل)**: توجيه الإشارة (البيانات) للوجهة المطلوبة عن طريق قفل **Switches** سواء في **Space domain** أو **Time domain** أو الاتنين.

## 2) ليه Switching أصلاً؟

الحل الأول: توصيل كل جهازين ببعض (**Mesh**) أو نجمة (**Star**) — **غير عملي ومهدر** لأن معظم اللينكات هتفضل فاضية معظم الوقت.

**الحل الأفضل: Switched Network** = سلسلة من العقد المتصلة (**Switches**) بتقدر تعمل اتصال مؤقت بين جهازين أو أكتر.

### تصنيف الشبكات المحولة (Switched Networks):

```
Switched Networks
├── Circuit-Switched Networks
├── Packet-Switched Networks
│   ├── Datagram Networks
│   └── Virtual-Circuit Networks
└── Message-Switched Networks
```

## 3) شبكات التبديل بالدوائر (Circuit-Switched Networks)

- اتصال بين محطتين = مسار **Dedicated** (مخصص) مكون من لينك واحد أو أكتر.
- كل لينك متقسم لـ **n قنوات** باستخدام **FDM** (تقسيم بالتردد) أو **TDM** (تقسيم بالزمن).
- الموارد بتتحجز في مرحلة الإعداد وتفضل مخصصة طول الاتصال.

### المراحل الثلاث (Three Phases):
| المرحلة | بيحصل إيه |
|---|---|
| **1. Setup Phase** | إنشاء الدائرة المخصصة قبل الاتصال |
| **2. Data Transfer Phase** | نقل البيانات بعد ما الدائرة اتعملت |
| **3. Teardown Phase** | إرسال إشارة لتحرير الموارد عند الانتهاء |

### مميزات وعيوب:
- ❌ **Efficiency منخفضة**: الموارد محجوزة طول الاتصال حتى لو مفيش بيانات بتتبعت.
- ✅ **Delay قليل جدًا**: البيانات مبتتأخرش عند كل Switch لأن الموارد محجوزة.

## 4) شبكات تبديل الرزم (Packet-Switched Networks)

- **مفيش حجز موارد مسبق** — الموارد بتتخصص **On Demand** بنظام **First Come, First Served**.
- البيانات بتتقسم لـ **Packets** صغيرة (~1000 octet)، كل Packet فيها جزء من البيانات + **Control Info** (معلومات توجيه/عنونة).
- كل Switch بيستقبل الـ Packet، يخزنها مؤقتًا (**Buffered**)، ويبعتها للعقدة التالية → ده اسمه **Store and Forward**.

### مميزات Packet Switching:
- ✅ **Line Efficiency** عالية: نفس اللينك بيتشارك بين Packets كتير
- ✅ **Data Rate Conversion**: كل محطة تتصل بالسرعة بتاعتها والـ Nodes بتعمل Buffering
- ✅ بيقبل Packets حتى وقت الازدحام (بس التسليم بيبطأ)
- ✅ ممكن تطبق **Priorities**

### طرقتين لمعالجة الـ Packets:

#### أ) Datagram (داتاجرام)
- كل Packet بتتعامل **بشكل مستقل**.
- كل Packet ممكن تمشي في **أي مسار**.
- ❌ ممكن توصل **خارج الترتيب** (Out of order)
- ❌ ممكن **تضيع** — والمستقبل هو المسؤول عن إعادة الترتيب والتعافي.

#### ب) Virtual Circuit (الدائرة الافتراضية)
- مسار **متخطط له قبل إرسال أي Packets**.
- **Call Request** و **Call Accept** بيعملوا اتصال (**Handshake**).
- كل Packet بيحمل **Virtual Circuit Identifier** بدل عنوان الوجهة.
- ✅ مفيش قرارات Routing لكل Packet.
- عند الانتهاء: **Clear Request** لإسقاط الدائرة.
- ⚠️ **مش Dedicated path** زي الـ Circuit Switching!

## 5) جدول مقارنة المحاضرة الثانية (احفظه كويس)

| وجه المقارنة | **Circuit Switching** | **Datagram Packet Switching** | **Virtual Circuit Packet Switching** |
|---|---|---|---|
| المسار | Dedicated transmission path | No dedicated path | No dedicated path |
| شكل البيانات | Continuous transmission | Transmission of packets | Transmission of packets |
| التخزين | الرسائل **مبتتخزنش** | Packets ممكن تتخزن لحد التسليم | Packets تتخزن لحد التسليم |
| المسار مُنشأ | طول المحادثة كلها | **لكل Packet لوحدها** | طول المحادثة كلها |
| التأخير | Call setup delay + transmission delay بسيط | Packet transmission delay | Call setup delay + packet delay |
| الازدحام | Overload ممكن يمنع الـ Call Setup بس مش بيأخر المكالمات القائمة | Overload بيزود Packet Delay | Overload ممكن يمنع Call Setup **و** يزود Packet Delay |
| التنبيه | Busy signal لو الطرف التاني مشغول | المرسَل ممكن يتنبه لو Packet ماوصلتش | المرسَل يتنبه لو الاتصال مرفوض |
| من مسؤول عن الفقد؟ | المستخدم مسؤول | الشبكة ممكن تكون مسؤولة عن كل Packet | الشبكة مسؤولة عن تسلسل الـ Packets |
| الـ Bandwidth | ثابت | استخدام ديناميكي | استخدام ديناميكي |
| Overhead Bits | مفيش بعد الـ Setup | في كل Packet | في كل Packet |

## 6) أوضاع الإرسال (Transmission Modes) — ثلاثة أنواع

```
Transmission Modes
├── Simplex Mode (اتجاه واحد)
├── Half-Duplex Mode (الاتنين بالتناوب)
└── Full-Duplex Mode (الاتنين في نفس الوقت)
```

| | **Simplex** | **Half-Duplex** | **Full-Duplex** |
|---|---|---|---|
| الاتجاه | اتجاه واحد بس (زي شارع اتجاه واحد) | الاتنين يقدروا يرسلوا ويستقبلوا **بس مش في نفس الوقت** | إرسال واستقبال **في نفس اللحظة** |
| أمثلة | Keyboard (إدخال بس)، Monitor (عرض بس) | Walkie-talkie | **Telephone Network** (الاتنين بيكلموا ويسمعوا في نفس الوقت) |
| التكلفة | الأرخص (قناة واحدة) | أقل من Full-Duplex | الأغلى (محتاج مسارين أو تقسيم السعة) |
| الموثوقية | الأسهل والأكثر موثوقية | أقل موثوقية من Full-Duplex | أعلى موثوقية ودقة |
| العيب | مفيش تأكيد وصول | تأخير بين الإرسال والاستقبال + محتاج تنسيق | معقد وغالي ومحتاج Bandwidth عالي |

> ملاحظة: في **Full-Duplex** المشاركة بتحصل بطريقتين: إما مسارين فيزيائيين منفصلين (واحد إرسال وواحد استقبال)، أو تقسيم سعة القناة بين الاتجاهين.

## 7) الكابلات في Cisco: Straight-Through vs Cross-Over

- **Straight-Through Cable**: نفس التوصيلة Pin 1 → Pin 1, Pin 2 → Pin 2 ... (نفس الألوان بالترتيب).
- **Cross-Over Cable**: الأطراف **بيتبادلوا** (Pin 1 → Pin 3, Pin 2 → Pin 6 ...).

### القاعدة العملية (متصِل بإيه؟):

| الجهاز A | الجهاز B | نوع الكابل |
|---|---|---|
| PC | Switch | **Straight-Through** |
| Switch | Switch | **Crossover** |
| PC | PC | **Crossover** |
| Router | Switch | **Straight-Through** |
| Router | Router | **Crossover** |
| Router | PC | **Crossover** |

> قاعدة سريعة للحفظ: **أجهزة مختلفة → Straight-Through | أجهزة زي بعض → Crossover** ✅

## 8) معماريات الشبكة (Network Architectures)

- **Client-Server**: سيرفر واحد أو أكتر بيقدموا خدمات للـ Clients (Request ←→ Response).
- **Peer-to-Peer (P2P)**: جهازين بنفس المستوى (**Peers**) كل واحد يرسل ويستقبل — Point-to-Point.
- **Hybrid**: خليط من الاتنين.

## 9) Line Configuration (تكوين الخط) — نوعان

### أ) Point-to-Point
- لينك **مخصص** بين جهازين بس.
- **السعة كلها** محجوزة لنقل البيانات بين الجهازين دول.

### ب) Multipoint (Multidrop)
- أكتر من جهازين بيتشاركوا **نفس اللينك**.
- السعة بتتقسم إما:
  - **Spatially shared**: أكتر من جهاز يقدر يستخدم اللينك في نفس الوقت
  - **Time-shared**: بالتناوب (كل واحد ياخد دوره)

## 10) الطوبولوجيا الفيزيائية (Physical Topology) — 4 أساسية

```
Topology
├── Mesh (شبكي)
├── Star (نجمة)
├── Bus (خط/حافلة)
└── Ring (حلقة)
```

### Mesh Topology (الشبكي)
- كل جهاز موصول بـ **Point-to-Point link لكل الأجهزة التانية**.
- عدد اللينكات في شبكة Mesh كاملة بـ n أجهزة = **n(n-1)/2** physical links.

| ✅ المميزات | ❌ العيوب |
|---|---|
| كل اتصال بحمله الخاص (مفيش مشاركة سعة) | كابلات كتير جدًا → تركيب وإعادة توصيل صعبة |
| Robust: عطل لينك واحد مش بيوقف النظام | حجم الأسلاك ممكن يعدي المساحة المتاحة |
| **Privacy & Security** عالية (كل رسالة في خط مخصص) | هاردوير الـ I/O Ports والكابلات غالي |
| سهولة تحديد وعزل الأعطال | |

### Star Topology (النجمة)
- كل جهاز موصول بـ Point-to-Point link **لجهاز مركزي واحد** بس (Hub/Switch/Bridge في Layer 2، Router/Gateway في Layer 3).
- مفيش اتصال مباشر بين الأجهزة — الـ **Controller** بيكون وسيط (Exchange).

| ✅ المميزات | ❌ العيوب |
|---|---|
| أرخص من Mesh (كل جهاز محتاج لينك واحد بس) | **العيب الأكبر**: اعتماد كلي على الـ Hub — لو وقع النظام كله يوقف |
| سهل التركيب وإعادة التهيئة (إضافة/حذف جهاز = تعديل اتصال واحد) | كل Node لازم يتوصل للمركزي |
| Robust: عطل لينك واحد بس بيتأثر | |

### Bus Topology (الحافلة)
- لينك واحد طويل (**Backbone**) بيربط كل الأجهزة — **Multipoint**.
- الأجهزة بتتصل بالـ Backbone عن طريق **Drop Line** (خط نازل) و **Tap** (وصلة بتتقارن أو بتخترق غلاف الكابل).
- الطرفين في **Terminator** بيمسح الإشارة من الخط.
- البيانات بتمشي في **اتجاه واحد** وبتضعف كل ما تمشي أبعد → فيه حد لعدد الـ Taps والمسافات.
- بيستخدم **CSMA/CD** عشان يتعامل مع مشكلة أكتر من Host بيبعتوا في نفس الوقت.

| ✅ المميزات | ❌ العيوب |
|---|---|
| سهولة التركيب + كابلات أقل من Mesh وStar | صعب إضافة أجهزة جديدة وعزل الأعطال |
| الـ Backbone بيمشي في أنسب مسار وكل Drop Line بيوصل لأقرب نقطة | **عطل في الـ Bus Cable بيوقف كل الإرسال حتى بين أجهزة على نفس الجهة** |
| | انعكاس الإشارة (**Signal Reflection**) عند الـ Taps بيسبب تدهور |

### Ring Topology (الحلقة)
- كل جهاز متوصل بـ Point-to-Point مع **الجيران الاتنين بس** (يمين وشمال).
- الإشارة بتمشي في الاتجاه الواحد (**Unidirectional**) أو الاتنين (**Bidirectional**) لحد ما توصل للوجهة.
- كل جهاز فيه **Repeater** بيجدد الـ Bits ويمررها.

| ✅ المميزات | ❌ العيوب |
|---|---|
| سهل التركيب والتهيئة: كل جهاز متوصل بجيرانه بس (إضافة/حذف جهاز = تعديل اتصالين) | **عطل أو قطع في الحلقة بيعطل الشبكة كلها** |
| | الحل: **Dual Ring** أو Switch بيقدر يقفل مكان القطع |

## 11) تصنيف الشبكات حسب الحجم

| | **LAN (Local Area Network)** | **WAN (Wide Area Network)** |
|---|---|---|
| المساحة | جوه مبنى واحد، إدارة واحدة | مساحة جغرافية كبيرة (مدينة/دولة/قارة) |
| السرعة | 10Mbps إلى 100Mbps (تقليديًا) | تكنولوجيات متقدمة: **ATM, Frame Relay, SONET** |
| عدد الأجهزة | محدود/صغير | كبير جدًا |
| الإدارة | Single administrative system | ممكن تكون تحت إدارات متعددة |
| مثال | **IEEE 802.3 (Ethernet)** | شبكات الاتصالات، بتربط LANs ببعض |

---

# 🧱 المحاضرة 3: نموذج الـ OSI والتغليف (Encapsulation)

## 1) إيه هو الـ OSI Model؟

**OSI (Open Systems Interconnection) Reference Model** = إطار مفاهيمي طوّرته منظمة **ISO** عشان يوصف وي standardize وظائف الاتصال في الشبكات.

⚠️ مهم جدًا: **الـ OSI مش Protocol في حد ذاته!** ده إطار مرجعي (Framework) لفهم وتصميم ومقارنة واستكشاف أخطاء الـ Protocols.

- بيقسم الاتصال لـ **7 طبقات**، كل طبقة مسؤولة عن مجموعة وظائف معينة.

### فوايد التقسيم للطبقات (Layering Benefits):
1. يقلل التعقيد بتقسيم المهام لأجزاء قابلة للإدارة
2. **Modularity**: كل طبقة لوظائف محددة
3. يبسّط استكشاف الأخطاء (تحدد الطبقة اللي فيها المشكلة)
4. يسهّل تطوير الـ Protocols
5. **Interoperability** بين تقنيات و vendors مختلفين
6. تغيير طبقة واحدة من غير ما تغير الباقي

## 2) الطبقات العليا والسفلى

- **Upper Layers (7, 6, 5)**: Application, Presentation, Session — بتخدم التطبيقات والتواصل بين الـ Processes. بتتسمى أحيانًا **Application Layers**.
- **Lower Layers (4, 3, 2, 1)**: Transport, Network, Data Link, Physical — مسؤولة عن نقل البيانات عبر الشبكة. بتتسمى **Data Flow Layers**.

> ⚠️ ملاحظة: "Application Layers" و "Data Flow Layers" **مش مصطلحات OSI رسمية** — دي للشرح بس.

## 3) المبادئ العامة (General Principles)
- كل طبقة بتقدم خدمات للطبقة اللي فوقها.
- كل طبقة بتستخدم خدمات الطبقة اللي تحتها.
- كل طبقة بتواصل منطقيًا مع نظيرتها (**Peer Layer**) على الجهاز التاني.
- عند الإرسال: **Encapsulation** (نزول الطبقات) — عند الاستقبال: **Decapsulation** (صعود الطبقات).

## 4) الطبقات السبع بالتفصيل ⭐ (أهم جدول في المحاضرة)

| # | الطبقة | الوظيفة | أمثلة |
|---|---|---|---|
| **7** | **Application** | واجهة بين الشبكة وبرامج التطبيق (بيستخدمها المستخدم) | **HTTP, FTP, SMTP, DNS, SNMP, Telnet** |
| **6** | **Presentation** | تمثيل وصيغة البيانات: ترجمة صيغ، **Encoding**, **Encryption/Decryption**, **Compression** | ASCII, EBCDIC, JPEG, MPEG |
| **5** | **Session** | إنشاء وصيانة جلسات الاتصال ثنائية الاتجاه، **Synchronization**، إدارة الـ Dialogs، إنهاء الجلسة | RPC, Session-management |
| **4** | **Transport** | اتصال **End-to-End** بين التطبيقات: **Segmentation & Reassembly**، **Multiplexing (Port Numbers)**، Flow Control، Error Recovery | **TCP** (موثوق Connection-Oriented)، **UDP** (Connectionless غير موثوق) |
| **3** | **Network** | توصيل **Packets** بين شبكات مختلفة: **Logical Addressing** + **Routing / Path Determination** | **IP**, IPX |
| **2** | **Data Link** | اتصال بين عقد متصلة مباشرة على نفس اللينك: **Framing**، **MAC Addressing**، **Media Access Control**، **Error Detection** | **Ethernet (IEEE 802.3)**, IEEE 802.2 LLC, HDLC |
| **1** | **Physical** | نقل الـ **Raw Bits** (0 و 1) عبر الوسط الفيزيائي: إشارات كهربائية/ضوئية/لاسلكية، جهد، Connectors، Pinouts، Bit Rate | EIA/TIA-232, V.35, Ethernet Physical |

### نقاط حفظ سريعة:
- **TCP** = Reliable + Connection-Oriented | **UDP** = Connectionless + من غير موثوقية مدمجة.
- الـ **IP** بيتسمى **Layer 3 Protocol** لأن وظائفه الأساسية بتطابق طبقة Network.
- الـ **Frame** في الـ Data Link = Header + Network-layer Packet + Trailer (الـ Trailer فيه غالبًا **FCS** لاكتشاف الأخطاء).

## 5) الـ PDU (Protocol Data Unit)

**PDU** = وحدة البيانات اللي بتتبادل بين طبقات الشبكة حسب البروتوكول الشغال عند الطبقة دي.

| الطبقة | اسم الـ PDU |
|---|---|
| Application / Presentation / Session | **Data** |
| Transport | **Segments** (TCP) / **Datagrams** (UDP) |
| Network | **Packets** |
| Data Link | **Frames** |
| Physical | **Bits** |

## 6) عملية التغليف (Encapsulation) — خطوة بخطوة

**Encapsulation** = إضافة معلومات تحكم خاصة بالبروتوكول للبيانات كل ما تنزل طبقة (على جهاز المرسل).

```
Data → Segment/Datagram → Packet → Frame → Bits
```

1. **Application Layer**: المستخدم بيكون البيانات (إيميل، طلب ويب...) والطبقة بتسلمها للطبقات الأدنى.
2. **Transport Layer**: بتقسم البيانات لـ **Segments** وبتضيف Transport Header (مثلاً TCP Header): Source Port, Destination Port, Sequence Number, Acknowledgment Info.
3. **Network Layer**: بتضيف **IP Header**: Source IP, Destination IP → الوحدة اسمها **IP Packet**.
4. **Data Link Layer**: بتضيف Header (Source/Destination MAC) + Trailer (FCS) → الوحدة اسمها **Frame**.
5. **Physical Layer**: بتحول الـ Frame لـ **Bits** وترسلها عبر الوسط الفيزيائي.

## 7) عملية فك التغليف (Decapsulation / De-encapsulation)

**العكس بالظبط** — بيحصل على جهاز المستقبل وهو بيصعد الطبقات:

```
Bits → Frame → Packet → Segment/Datagram → Data
```

1. **Physical**: يستقبل الإشارات ويحولها Bits → يسلمها للـ Data Link. (Bits → Frame)
2. **Data Link**: يفحص الـ Destination MAC ويعمل Error Detection بـ FCS، لو الـ Frame سليم وموجه له يشيل الـ Header/Trailer ويسلم الـ Packet للـ Network. (Frame → Packet)
3. **Network**: يعالج الـ IP Header (الـ Destination IP) ويشيله ويسلم للـ Transport. (Packet → Segment)
4. **Transport**: يعالج الـ Header (Ports, Sequence/Ack في TCP) ويشيله ويسلم البيانات للتطبيق. (Segment → Data)
5. **Upper Layers**: Session و Presentation و Application بيعملوا وظائفهم (فك التشفير، فك الضغط، تحويل الصيغ...) ويسلموا البيانات الأصلية للتطبيق.

| العملية | الاتجاه | الفكرة |
|---|---|---|
| **Encapsulation** | Upper → Lower | إضافة Headers/Trailers |
| **Decapsulation** | Lower → Upper | معالجة وإزالة Headers/Trailers |

## 8) الطبقة الفيزيائية (Physical Layer) بالتفصيل

- أدنى طبقة في الـ OSI، مسؤولة عن نقل **Raw Bits** بين الأجهزة.
- **مش فاهمة معنى البيانات** — بتهتم فقط بتمثيل البتس وإرسالها واستقبالها كإشارات.
- بتربط بين الـ Data Link Layer والوسط الفيزيائي.

**وظائفها:**
| الوظيفة | الشرح |
|---|---|
| **Bit Transmission** | إرسال Raw Bits بين الأجهزة |
| **Signal Representation** | تمثيل الـ Bits بإشارات كهربائية/ضوئية/راديو |
| **Encoding** | إزاي البتس بتمثل بأنماط الإشارة |
| **Modulation** | تعديل إشارة حاملة (**Carrier**) لتحمل معلومات |
| **Data Rate** | معدل إرسال البتس |
| **Synchronization** | مساعدة المرسل والمستقبل على تحديد حدود البتس |
| **Physical Interfaces & Connectors** | مواصفات التوصيلات الفيزيائية |
| **Transmission Modes** | Simplex, Half-Duplex, Full-Duplex |
| **Physical Topology** | الترتيب الفيزيائي للتوصيلات |

**أمثلة تقنيات:** Ethernet, Wi-Fi, Fiber-optic, DSL, Cellular.
**منظمات المعايير:** IEEE, ITU-T, ISO, ANSI.

## 9) الـ Hub

- **Hub** = جهاز بسيط شغال في **Layer 1 (Physical)** — هو في الأساس **Multi-port Repeater**.
- بيستقبل الإشارة على بورت و**يجددها ويبعتها لكل البورتات التانية** بغض النظر عن الجهاز المقصود.
- ❌ **مش بيفحص** MAC Addresses ولا IP Addresses ولا Frames ولا Packets.
- **Collision Domain**: كل الأجهزة المتوصلة على الـ Hub بتتشارك **Collision Domain واحد** — لو جهازين بعتؤا في نفس الوقت الإشارات بتتداخل ويحصل **Collision**.
- ⚠️ **Security Consideration**: لأن الـ Hub بيبعت الإشارة لكل البورتات، أي حد متوصل يقدر يراقب الـ Traffic — مفيش **Traffic Isolation**. عشان كده أقل خصوصية وأقل أمان من الـ Switch.

---

# 🔗 المحاضرة 4: طبقة الـ Data Link (Layer 2)

## 1) مقدمة

**Data Link Layer (Layer 2)** = تاني طبقة في الـ OSI. بتحدد إزاي البيانات بتتنظم في **Frames** وبتتبادل بين الأجهزة المتصلة على **نفس الشبكة المحلية (Local Network)**.

**الفرق بين Layer 1 و Layer 2 (افهمه كويس):**
- **Physical Layer (L1)**: بترسل و تستقبل **Raw Bits** على الوسط الفيزيائي.
- **Data Link Layer (L2)**: بتنظم الـ Bits في **Frames** وبتدير توصيلها عبر الشبكة المحلية.

مثال: لما كمبيوتر بيبعت **IP Packet** على شبكة Ethernet، الـ Data Link Layer بتغلف الـ Packet جوه **Ethernet Frame** فيه: **Source MAC** + **Destination MAC** + **Error-Detection** معلومات.

### مصطلحات الـ PDU (مهمة):
- Data Link Layer → الـ PDU اسمها **Frame**
- Network Layer → الـ PDU اسمها **Packet**
- Physical Layer → بترسل **Bits**

## 2) الوظائف الرئيسية للـ Data Link Layer (6 وظائف)

### أ) Framing (التأطير)
- تنظيم البيانات الجاية من الطبقة اللي فوق (Network) في وحدة منظمة اسمها **Frame**.
- الـ Frame عادةً بتحتوي: **Header** (عناوين مصدر ووجهة) + **Payload** (البيانات المغلفة) + **Trailer** (حسب التقنية).
- الفايدة: المستقبل يعرف **فين بداية ونهاية** وحدة البيانات.

### ب) Media Access Control (MAC)
- لما أجهزة كتير بتتشارك وسط نقل واحد، محتاجين قواعد بتحدد **مين يبعت امتى** — دي بتسمى **Media Access Control Mechanisms**.
- مثال: الـ Ethernet القديم كان بيستخدم **CSMA/CD**، و Wi-Fi بيستخدم **CSMA/CA**.
- في الـ Modern Switched Ethernet (Full-Duplex)، كل جهاز عنده لينك مخصص للـ Switch → مفيش تنافس على نفس الوسط.

### ج) Addressing (العنونة)
- الـ Data Link Layer بيستخدم **Physical Addresses** (اللي معروفة بـ **MAC Addresses** في Ethernet) عشان يحدد الـ Network Interfaces على الشبكة المحلية.
- الـ **Destination MAC Address** بيساعد الجهاز أو الـ Switch يحدد هل الـ Frame تتقبل ولا لأ.

### د) Error Detection (اكتشاف الأخطاء)
- الإرسال ممكن يسبب **Bit Errors** بسبب الضوضاء (Noise) والتداخل.
- كتير من بروتوكولات Layer 2 بتستخدم آلية اكتشاف أخطاء عشان تعرف لو الـ Frame اتلفت ولا لأ.
- مثال: Ethernet بيستخدم **Frame Check Sequence (FCS)** مبني على **Cyclic Redundancy Check (CRC)**.
- ⚠️ مهم: **Error Detection ≠ Retransmission** — اكتشاف الخطأ مش معناه إن Layer 2 هيعيد الإرسال بالضرورة.

### هـ) Identification of Encapsulated Data (تحديد البيانات المغلفة)
- الـ Frame ممكن يحمل بيانات لبروتوكولات عليا مختلفة → المستقبل محتاج يعرف **أنبني بروتوكول** يعالج الـ Payload.
- مثال: **Ethernet II** بيستخدم حقل **EtherType** عشان يحدد بروتوكولات زي **IPv4, ARP, IPv6**.

### و) Flow and Error Control (التحكم في التدفق والأخطاء)
- بعض بروتوكولات Layer 2 بتوفّر **Flow Control** أو **Error Recovery** أو الاتنين — لكن دي خدمات **تعتمد على البروتوكول** ومش كل Layer 2 بيوفرها بنفس الطريقة.
- مثال: الـ FCS في Ethernet بيكتشف الـ Frames التالفة، **لكن** الـ Ethernet العادي **مش بيعيد إرسال** الـ Frames التالفة على مستوى الـ MAC Layer.

## 3) الـ Sublayers في الـ IEEE 802: LLC و MAC

```
┌─────────────────────────────────┐
│  Logical Link Control (LLC)     │  ← واجهة بروتوكولات الطبقات العليا + وظائف تحكم
├─────────────────────────────────┤
│  Media Access Control (MAC)     │  ← MAC addressing, frame handling, الوصول للوسط
├─────────────────────────────────┤
│  Physical Layer                 │  ← إشارات ووسط وبتس
└─────────────────────────────────┘
```

### MAC Sublayer
بتتعامل مع: الوصول لوسط النقل، تعريف **MAC Addressing** واستخدامه، إدارة الوصول للوسط المشترك (لو محتاج)، دعم إرسال واستقبال الـ Frames، توفير معلومات Error Detection (زي FCS).

### LLC Sublayer
- بتوفّر **واجهة منطقية** بين خدمات الـ IEEE 802 Data Link والـ Network Layer.
- بتساعد في تحديد بروتوكولات الطبقات العليا ودعم خدمات الـ Link Control.
- ⚠️ **Technical Note**: مش كل تحديد البيانات المغلفة بيتعمل عن طريق LLC — الـ **Ethernet II** بيستخدم حقل **EtherType** مباشرة.

## 4) طرق الـ MAC (Media Access Control) — وتقسيم الوسط

طريقة التحكم في الوصول للوسط بتعتمد على حاجتين:
1. **Media Sharing**: هل أجهزة كتير بتستخدم نفس الوسط ولازم تنسق إرسالها؟
2. **Topology**: إزاي الأجهزة متوصلة.

لما أجهزة كتير تبعت على نفس الوسط المشترك من غير تنسيق → الإشارات بتتداخل → **Collision**.

### الفئتين الكبار:

```
MAC Methods
├── Controlled Access (وصول متحكم فيه)
│   ├── Reservation (حجز أوقات مسبق)
│   ├── Polling (تحكم مركزي يسأل كل جهاز)
│   └── Token Passing (التوكن بيدور واللي معاه يبعت)
└── Contention-Based Access (وصول بالتنافس)
    ├── ALOHA
    ├── CSMA
    ├── CSMA/CD (Ethernet قديم)
    └── CSMA/CA (Wi-Fi)
```

| الميزة | **Controlled Access** | **Contention-Based Access** |
|---|---|---|
| آلية الوصول | وصول منسق | الأجهزة بتتنافس |
| إمكانية الـ Collision | غالبًا **ممنوعة** بالآلية | **ممكنة** |
| الانتظار | ممكن ينتظر إذن أو دور | ممكن ينتظر أو يعمل Backoff أو يعيد الإرسال |
| أمثلة | Polling, Token Passing, Reservation | ALOHA, CSMA/CD, CSMA/CA |
| التطبيق النموذجي | شبكات Token-based وأنظمة مجدولة | Ethernet المشترك تاريخيًا؛ Wi-Fi |

### Controlled Access — الطرق:
- **Reservation**: الأجهزة بتحجز **Time Slots** قبل الإرسال.
- **Polling**: **Central Controller** بيسأل كل جهاز بالدور لو معاه بيانات يبعتها.
- **Token Passing**: إطار تحكم خاص اسمه **Token** بيدور بين الأجهزة — **اللي معاه التوكن بس هو اللي يقدر يبعت**.

## 5) ALOHA

طريقة Random-Access بسيطة وقديمة طُورت لشبكات الـ Packet-Radio.

### Pure ALOHA (سلوك الإرسال):
1. المحطة تبعت الـ Frame على طول لما يكون جاهز.
2. المستقبل بيفحص الـ Frame ويبعت **Acknowledgment (ACK)**.
3. المرسَل بينتظر الـ ACK.
4. لو الـ ACK ماوصلش في الوقت المتوقع → يفترض إن الإرسال فشل.
5. بينتظر **فترة عشوائية** ويعيد الإرسال (حد أقصى لعدد المحاولات).

- لو محطتين بعتوا في أوقات متداخلة → الـ Frames بتتصادم وتبوظ.
- ✅ ميزة: **البساطة** | ❌ عيب: كفاءة قناة منخفضة لأن الإطارات ممكن تتداخل في أي وقت.
- **الحد الأقصى النظري للإنتاجية: ~18.4%** من سعة القناة.

### Slotted ALOHA:
- الوقت متقسم لـ **Slots متساوية** (كل Slot = زمن إرسال Frame واحد).
- الإرسار بيبدأ **بس عند بداية الـ Slot**.
- ✅ بيقلل احتمالات التصادم لأن الإرسال متزامن مع حدود الـ Slots.
- ❌ ممكن محطتين يختاروا نفس الـ Slot ويحصل تصادم برضه.
- **الحد الأقصى النظري: ~36.8%** = **ضعف** الـ Pure ALOHA.

| الميزة | **Pure ALOHA** | **Slotted ALOHA** |
|---|---|---|
| بداية الإرسال | في أي وقت | عند حدود الـ Slot |
| التزامن (Synchronization) | غير مطلوب | مطلوب |
| احتمالية التصادم | أعلى | أقل |
| أقصى إنتاجية نظرية | ~18.4% | ~36.8% |

## 6) CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

كانت بتستخدم في **Ethernet القديم المشترك (Shared, Half-Duplex)**. الاسم معناه ثلاث حاجات:
- **Carrier Sense**: المحطة بتحس هل الوسط شغال (Busy) ولا فاضي (Idle).
- **Multiple Access**: كذا محطة بتتشارك نفس الوسط.
- **Collision Detection**: المحطة المرسِلة بتقدر **تكتشف التصادم أثناء الإرسال**.

**على عكس ALOHA**: CSMA/CD بيحاول تقلل التصادمات بالتحقق من الوسط **قبل** الإرسال، ويقلل الوقت المهدر باكتشاف التصادم أثناء الإرسال.

### خطوات CSMA/CD:
1. **تحسس الوسط**: هل القناة Idle ولا Busy؟
2. **الإرسال لما تفضى**: لو Busy نستنى لحد ما تفضى.
3. **مراقبة أثناء الإرسال**: المحطة فاضلة بتراقب لاكتشاف أي Collision.
4. **إشارة التصادم**: لو اكتشفت Collision تبعت **Jamming Signal** وتوقف الإرسال.
5. **Backoff وإعادة المحاولة**: تستنى فترة عشوائية محددة بطريقة **Binary Exponential Backoff** قبل ما تحاول تاني.

### ⚠️ ليه CSMA/CD مش بتستخدم في Ethernet الحديث؟
- الـ **Hubs** القديمة ببتكّن **Shared Collision Domain** واحد.
- الـ **Ethernet Switch** بيخلق لينكات منفصلة، والـ Ethernet المُبدَّل الحديث بيشتغل **Full-Duplex**.
- على لينك Full-Duplex الجهاز يقدر يرسل ويستقبل في نفس الوقت **من غير تنافس** على وسط معرض للتصادم → **CSMA/CD مش محتاجة**.
- عشان كده CSMA/CD مهمة بس كدراسة تاريخية لـ Ethernet القديم.

## 7) CSMA/CA (في Wi-Fi)

- Wi-Fi بيستخدم **CSMA/CA = Collision Avoidance** مش CD.
- محطات الوايرلس **مش بتقدر تكتشف التصادم بشكل موثوق أثناء الإرسال** زي الـ Ethernet السلكي.
- بدل كده بيستخدم: **Channel Sensing** + **Waiting Periods** + **Randomized Backoff** + آليات تانية عشان **يتجنب** احتمال الإرسال المتزامن.

## 8) FDDI (Fiber Distributed Data Interface)

- تقنية LAN تاريخية عالية السرعة باستخدام **Fiber-Optic** و **Token Passing**.
- الخصائص الرئيسية:
  - معدل بيانات اسمي **100 Mbps**.
  - معمارية **Dual-Ring**.
  - **Token Passing** للتحكم في الوصول للوسط.
  - آليات تحمل أعطال، منها **Ring Wrapping** عند حدوث أعطال معينة.
  - دعم شبكات كبيرة.
- ⚠️ ملاحظة تعليمية: FDDI مثال **تاريخي** مفيد للدراسة، لكن **مش** بديل حديث مهيمن — Ethernet الحديث استبدلها في معظم الشبكات المعاصرة.

## 9) Ethernet (IEEE 802.3)

**Ethernet** = عائلة تقنيات LAN موحّدة أساسًا تحت **IEEE 802.3**. بتحدد خصائص الطبقة الفيزيائية **والـ Data Link Layer** (Framing و MAC).
مستخدمة على نطاق واسع: شبكات المكاتب، الحرم الجامعي، مراكز البيانات، البيوت.

### بنية الـ Ethernet II Frame (احفظها بالأرقام دي!):

```
| Destination MAC | Source MAC | EtherType | Payload        | FCS   |
|    6 bytes      |  6 bytes   |  2 bytes  |  46-1500 bytes | 4 bytes|
```

- لـ Frame Ethernet قياسي بدون Tags، **مستبعدين الـ Preamble و Start Frame Delimiter**.
- **VLAN Tagging** بيغير حجم الـ Header وحجم الـ Frame المسموح.

**حقول الـ Frame:**
- **Destination MAC Address**: بيحدد الوجهة (جهاز أو مجموعة).
- **Source MAC Address**: بيحدد الواجهة المرسِلة.
- **EtherType**: بيحدد البروتوكول المغلف في Ethernet II.
- **Payload**: البيانات المغلفة — ممكن يضاف **Padding** عشان يتحقق الحد الأدنى لحجم الـ Frame.
- **FCS**: قيمة اكتشاف الخطأ المحسوبة بـ **CRC**.

### الـ MAC Addressing:
- الـ **MAC Address** = عنوان طبقة ربط بيحدد واجهة شبكة في نطاق Layer 2.
- عنوان Ethernet تقليدي = **48 bits (6 bytes)** مكتوب غالبًا كـ **12 رقم Hexadecimal**.
- مثال: `00:00:0C:12:34:56` — وممكن يتكتب بالصيغة المنقطة Cisco: `0000.0C12.3456`.

### أنواع عناوين MAC:

| النوع | الوصف |
|---|---|
| **Unicast** | بيحدد **واجهة واحدة** — الـ Frame موجه لجهاز واحد بس |
| **Broadcast** | العنوان: `FF:FF:FF:FF:FF:FF` — الـ Frame موجه **للكل** في الـ Broadcast Domain. الـ Switch عادة بيعمل **Flood** للـ Broadcast Frames لكل البورتات المؤهلة في نفس الـ VLAN (ما عدا بورت الوصول) |
| **Multicast** | بيحدد **مجموعة** واجهات — إرسال واحد لمجموعة مستقبلين مهتمين. الـ Switches ممكن تستخدم **IGMP Snooping** عشان تقلل الـ Multicast Forwarding غير الضروري. لـ IPv4 Multicast على Ethernet: الوجهة بتبدأ بـ `01:00:5E` — والـ Mapping بيغطي **جزء** بس من فضاء الـ IPv4 Multicast (فمجموعات IP مختلفة ممكن تتطابق على نفس عنوان MAC) |

> ⚠️ فرق أساسي: **MAC Addresses** بتخدم توصيل طبقة الربط (Link-Layer Delivery)، و **IP Addresses** بتخدم العنونة المنطقية والـ **Routing** بين الشبكات المختلفة.

## 10) اكتشاف الأخطاء: FCS و CRC

- الـ Physical Transmission ممكن يتأثر بالـ **Noise, Interference, Attenuation** → تغيير في الـ Bits.
- كتير من بروتوكولات Layer 2 بتحط حقل Error-Detection في الـ Frame أو الـ Trailer.

### آلية FCS (Frame Check Sequence) — 4 خطوات:
1. المرسِل يحسب قيمة **CRC** من محتويات الـ Frame.
2. المرسِل يحط القيمة المحسوبة في حقل **FCS**.
3. المستقبل يعمل نفس الفحص على الـ Frame المستلم.
4. لو الفحص أظهر خطأ → الـ Frame يتعتبر تالف وعادة **يتُرمى** (Discard) من أجهزة Ethernet.

> **CRC vs FCS**: CRC هي **طريقة الحساب**، و FCS هو **حقل الـ Frame** اللي بيحمل نتيجة الفحص.

### Error Detection ≠ Error Recovery:
- **Error Detection**: تحديد إن البيانات ممكن تكون اتلفت.
- **Error Recovery**: اتخاذ إجراء للحصول على البيانات الصح (زي إعادة الإرسال).
- الـ Ethernet العادي **مش بيعيد إرسال** الـ Frames التالفة على مستوى MAC — الاسترداد ممكن يحصل في طبقة أعلى، مثلاً **TCP** يقدر يكتشف البيانات المفقودة/التالفة ويرتب إعادة الإرسال.

### جدول EtherType الشهير:

| EtherType | البروتوكول المغلف |
|---|---|
| `0x0800` | **IPv4** |
| `0x0806` | **ARP** |
| `0x86DD` | **IPv6** |

(مثال: لو EtherType = 0x0800 → الواجهة المستقبلة بتعرف إن الـ Payload فيه IPv4 وتسلمه لمعالج IPv4.)

## 11) الـ Layer 2 Switches

**Layer 2 Switch** = جهاز شبكة بيمرّر **Ethernet Frames** باستخدام **MAC Addresses**.

**الفرق عن الـ Hub:** الـ Hub بيكرر الإشارات لكل البورتات، أما الـ Switch **بيتعلم** إيه عناوين MAC الموجودة ورا كل بورت ويستخدم المعلومة دي في توجيه الـ Frames.

### إزاي الـ Switch بيتعلم العناوين؟
- الـ Switch بيبني **MAC Address Table** عن طريق فحص **Source MAC Address** للـ Frames الواردة.
- مثال: لو Frame وصلت على **Port 1** ومصدرها `00:11:22:33:44:55` → الـ Switch يسجل إن العنوان ده reachable عن طريق Port 1.
- الـ Switch بيكدّث الإدخالات مع وصول الـ Traffic، والإدخالات الديناميكية غير النشطة بتتحذف بعد فترة (**Aging Out**).

### خطوات تمرير الـ Frame (5 خطوات):
1. استقبال الـ Frame.
2. تعلّم/تحديث الـ Source MAC + البورت الواصل منه.
3. فحص الـ Destination MAC.
4. البحث في الـ MAC Address Table.
5. تمرير الـ Frame عبر البورت المناسب، **أو** فلترتها لو الوجهة reachable من نفس البورت الواصل، **أو** عمل **Flood** لو العنوان مجهول.

> الـ **Unknown-Unicast** و **Broadcast** Frames بتتعمل Flood عادة داخل الـ VLAN المخصصة (حسب إعدادات الـ Switch والأمان).

## 12) Collision Domains و Broadcast Domains

- الـ **Switch بيفصل Collision Domains** بين بورتات Ethernet المختلفة. في الـ Full-Duplex Switched Ethernet الحديث، التصادمات **مش بتحصل** أصلاً.
- ⚠️ لكن الـ Layer 2 Switch **مش بيعمل** Broadcast Domain منفصلة لكل بورت تلقائيًا. الأجهزة في نفس الـ **VLAN** بتتشارك نفس الـ Broadcast Domain. الـ **VLANs** بتستخدم لتقسيم الشبكة المُبدَّلة لـ Broadcast Domains منفصلة.

## 13) طرق التبديل في السويتشات (3 طرق — جدول مهم)

| الميزة | **Store-and-Forward** | **Cut-Through** | **Fragment-Free** |
|---|---|---|---|
| بيستقبل الـ Frame كله الأول؟ | ✅ Yes | ❌ No | ❌ No |
| يقدر يتحقق من الـ FCS قبل التمرير؟ | ✅ Yes | ❌ مش بالضرورة | ❌ No |
| زمن التمرير (Latency) | أعلى عمومًا | أقل عمومًا | متوسط |
| الفكرة الأساسية | **التحقق من الـ Frame** | **زمن تأخير منخفض** | **حل وسط تاريخي** |

### شرح كل طريقة:
- **Store-and-Forward**: الـ Switch بيستقبل ويخزن الـ Frame كله قبل تمريره ويقدر يفحص الـ FCS.
  - ✅ مميزات: يرمي الـ Frames اللي FCS بتاعها غلط، تحقق موثوق قبل التمرير، يقدر يتعامل مع اختلاف السرعات بين البورتات عن طريق الـ Buffering.
  - ❌ عيب: لازم يستقبل الـ Frame كامل → زمن تأخير أعلى من Cut-Through.
- **Cut-Through**: بيبدأ التمرير بعد ما يقرأ **جزء كافي من الـ Header** عشان يعرف الوجهة.
  - ✅ ميزة: زمن تأخير أقل للـ Traffic المؤهل.
  - ❌ عيب: الـ Frame التالف ممكن يبدأ يتمرر قبل ما الـ Switch يستقبله كامل ويفحصه → ممكن ينشر الـ Bad Frames اللي الـ Store-and-Forward كانت هترميها.
- **Fragment-Free**: حل وسط تاريخي — بيستنى أول **64 bytes** قبل التمرير، عشان يتجنب تمرير شظايا التصادم (Collision Fragments) المرتبطة بالـ Ethernet المشترك القديم.

## 14) أنواع الـ Switches (تصنيفات — مش متبادلة الإقصاء)

### أ) حسب الـ OSI Layer:
| النوع | الوصف |
|---|---|
| **Layer 2 Switch** | يمرر Ethernet Frames باستخدام MAC Addresses — لتوصيل الأجهزة النهائية جوه LAN أو VLAN |
| **Layer 3 Switch** | يدعم Layer 2 Switching + وظائف Layer 3 — يقدر يمرر IP Packets بين VLANs أو Subnets عند تهيئته |

### ب) حسب الإدارة:
- **Unmanaged Switch**: محتاج إعدادات قليلة أو معدومة، لشبكات صغيرة/بسيطة، مراقبة وتحكم محدودين.
- **Managed Switch**: فيه إعدادات ومراقبة — ممكن يدعم **VLANs, QoS, Link Aggregation, Access Controls** وغيرها.
- **Smart Switch**: إدارة أقل من الـ Managed الكامل، والمميزات بتختلف حسب الشركة المصنعة.

### ج) حسب طريقة التبديل:
- **Store-and-Forward** / **Cut-Through** / **Fragment-Free** (اتشرحوا فوق).

### د) حسب التصميم الفيزيائي:
- **Fixed-Configuration Switch**: عدد ثابت من البورتات ومش بيدعم توسعة عبر وحدات قابلة للتبديل.
- **Modular Switch**: يدعم التوسعة/التهيئة عن طريق Modules — شائع حيث التوسعية ومرونة البورتات مهمة.

### هـ) حسب القدرة على الطاقة (PoE):

| نوع الـ Switch | الوصف | التطبيقات النموذجية |
|---|---|---|
| **Non-PoE** | بيانات بس — **مش** بيورد طاقة من البورتات | PCs, Printers, Servers |
| **PoE** | بيانات + طاقة على نفس كابل Ethernet | IP Cameras, VoIP Phones, Wireless APs |
| **PoE+** | مستوى طاقة أعلى من PoE القياسي | كاميرات متقدمة، APs ثنائية النطاق |
| **PoE++** | طاقة أعلى للأجهزة المستهلكة | Wi-Fi 6/7 APs, PTZ Cameras, Digital Signage |

### و) حسب تصميم الشبكة (الطبقات الهرمية الثلاث):

```
        [ Core Switch ]          ← العمود الفقري عالي السرعة
              │
      ┌───────┴───────┐
   [Distribution]   [Distribution]  ← تجميع Access Switches + سياسات
    │      │          │      │
 [Access] [Access] [Access] [Access] ← توصيل الأجهزة النهائية
   PCs   Printers    PCs     WiFi
```

- **Access Switch**: يوصل الأجهزة النهائية (PCs, Printers, IP Phones, APs).
- **Distribution Switch**: يجمع الـ Access Switches وقد يعمل **Inter-VLAN Routing** + **Access Control** + **QoS**.
- **Core Switch**: توصيل عالي السرعة بين الأجزاء الرئيسية للشبكة — الموثوقية والسعة والتكرار (Redundancy) مهمة.

> **تشبيه للحفظ:** Access = مدخل البناية اللي بيوصل المستخدمين | Distribution = الممر اللي بيوصل الأدوار | Core = الطريق السريع الرئيسي.
> ⚠️ دي **أدوار تصميم** مش طبقات OSI منفصلة — نفس الـ Switch ممكن يعمل أكتر من دور.

## 15) Hub vs Layer 2 Switch (جدول مقارنة ختامي)

| الميزة | **Hub** | **Layer 2 Switch** |
|---|---|---|
| التشغيل في OSI | **Layer 1 (Physical)** | **Layer 2 (Data Link)** |
| سلوك التمرير | **يكرر الإشارات** لكل البورتات التانية | يمرر **Frames** بناءً على **MAC Addresses** |
| Collision Domains | **Collision Domain واحد مشترك** | **Collision Domain منفصل لكل بورت** |
| التشغيل النموذجي | Half-Duplex (وسط مشترك) | Full-Duplex عادة |
| استخدام الـ Bandwidth | **مشترك** بين كل الأجهزة المتصلة | سعة مخصصة لكل بورت (خاضعة لسعة الـ Uplink) |

> خلاصة سريعة: الـ **Hub** **مش بيفحص** MAC Addresses أصلاً، والـ **Layer 2 Switch** بيتعلم MAC Addresses ويستخدمها في تمرير الـ Frames. ✅

---

# 🎯 ملخص شامل سريع للمراجعة النهائية

## سلسلة التغليف:
```
Data → Segment/Datagram → Packet → Frame → Bits
Bits → Frame → Packet → Segment/Datagram → Data
```

## أسماء الـ PDU حسب الطبقة:
Data (App/Pres/Sess) → Segment/Datagram (Transport) → Packet (Network) → Frame (Data Link) → Bits (Physical)

## أهم الفروقات اللي لازم تحفظها:
1. **Circuit Switching** (موارد محجوزة، تأخير قليل، كفاءة منخفضة) vs **Packet Switching** (من غير حجز، محتمل تأخير، كفاءة عالية)
2. **Datagram** (كل Packet لوحدها، ممكن تضيع/تتوصل مش مرتبة) vs **Virtual Circuit** (مسار مُنشأ مسبقًا، VCI بدل العنوان)
3. **Simplex** (اتجاه واحد) vs **Half-Duplex** (بالتناوب) vs **Full-Duplex** (في نفس الوقت)
4. **Mesh/Star/Bus/Ring** — المميزات والعيوب
5. **TCP** (موثوق) vs **UDP** (غير موثوق)
6. **MAC Address** (Link-Layer) vs **IP Address** (Logical/Routing)
7. **Pure ALOHA (18.4%)** vs **Slotted ALOHA (36.8%)**
8. **CSMA/CD** (كشف التصادم — Ethernet قديم) vs **CSMA/CA** (تجنب التصادم — Wi-Fi)
9. **Error Detection** (اكتشاف) vs **Error Recovery** (استرداد — زي TCP)
10. **Store-and-Forward** (تحقق + تأخير أعلى) vs **Cut-Through** (سرعة + احتمال تمرير أخطاء) vs **Fragment-Free** (وسط تاريخي)
11. **Hub** (L1، يكرر، Collision Domain واحد) vs **Switch** (L2، MAC Table، بيفصل Collision Domains)
12. الـ **Switch بيفصل Collision Domains** لكن **مش بيفصل Broadcast Domains** — الـ VLAN هي اللي بتفصل Broadcast Domains
13. **Straight-Through** (أجهزة مختلفة) vs **Crossover** (أجهزة زي بعض)
14. **Controlled Access** (منسق) vs **Contention-Based** (تنافسي)
15. **Unicast** (جهاز واحد) vs **Broadcast** (الكل FF:FF:FF:FF:FF:FF) vs **Multicast** (مجموعة 01:00:5E...)
16. **Throughput ≤ Information Rate ≤ Data Rate ≈ Bit Rate ≤ Link Rate**

بالتوفيق! 🚀
