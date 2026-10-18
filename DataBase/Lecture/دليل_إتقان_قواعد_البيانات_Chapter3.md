# 🗄️ دليل إتقان قواعد البيانات — Database Mastery Guide
### مبني على Chapter 3 (ER Model) + مراجعة شاملة لجميع الأبواب السابقة
> **لغة الملف:** عربي (RTL) + إنجليزي مدمج — كل مصطلح يظهر بالإنجليزي لأنه ده اللي هييجي في الامتحان

---

# 🧭 خريطة الطريق الكاملة (Roadmap)

```
المستوى 0: Data → Database → DBMS → Database System
المستوى 1: Database Design Process (Requirements → Conceptual → Logical → Physical)
المستوى 2: ER Model (Entities, Attributes, Relationships, Constraints)
المستوى 3: Mapping (تحويل ERD → Relational Schema → SQL)
المستوى 4: SQL + Keys + Normalization + Transactions + Indexes
```

---

# 📘 المستوى 0: الصورة الكبيرة (The Big Picture)

## 1. الفرق بين المفاهيم الأربعة (أساس كل حاجة)

| المصطلح | المعنى | مثال من المستشفى |
|---|---|---|
| **Data** | البيانات الخام نفسها | اسم المريض `أحمد`، رقم ملفه `101` |
| **Database** | مجموعة **منظمة ومترابطة** من البيانات | بيانات المرضى + الأطباء + المواعيد + الفواتير |
| **DBMS** | البرنامج اللي **يدير** قاعدة البيانات (تخزين/استرجاع/صلاحيات) | Oracle, PostgreSQL |
| **Database System** | الصورة الأشمل: DB + DBMS + Applications + Users | التطبيق + الـ DBMS + الموظفين |

> 🔑 **الجملة اللي تجيب عليها أي سؤال نظري:**
> *"The DBMS mediates between users/applications and the database — it enforces constraints and controls access."*

## 2. رحلة البيانات (Data Journey)

```
User → Application → SQL Command → DBMS (يتحقق من Constraints + Permissions)
    → Database → Result ترجع بنفس الطريق عكسيًا
```

---

# 🏗️ المستوى 1: عملية تصميم قاعدة البيانات (Database Design Process)

دي أول صورة مهمة في المحاضرة (Figure 3.1)، وبتيجي سؤال كتير:

```
                    ┌─────────────┐
                    │  Miniworld  │  (العالم الحقيقي المصغّر)
                    └──────┬──────┘
                           ▼
              ┌─────────────────────────┐
              │ REQUIREMENTS COLLECTION │  ← جمع المتطلبات
              │       AND ANALYSIS      │
              └───────────┬─────────────┘
            ┌─────────────┴─────────────┐
            ▼                           ▼
  ┌───────────────────┐       ┌───────────────────┐
  │ FUNCTIONAL        │       │ CONCEPTUAL DESIGN │  ← تصميم مفاهيمي
  │ ANALYSIS          │       │ (Conceptual Schema│     (ERD هنا!)
  │ (High-Level       │       │  - high-level     │
  │  Transactions)    │       │  data model)      │
  └─────────┬─────────┘       └─────────┬─────────┘
            │                           ▼
            │ DBMS-independent   ┌───────────────────┐
            │ ◄──────────────►   │ LOGICAL DESIGN    │  ← Data Model
            │ DBMS-specific      │ (Data Model       │     Mapping
            │                    │  Mapping)         │
            │                    └─────────┬─────────┘
            ▼                              ▼
  ┌───────────────────┐            ┌───────────────────┐
  │ APPLICATION       │            │ PHYSICAL DESIGN   │  ← التخزين الفعلي
  │ PROGRAM DESIGN    │            │ (Internal Schema) │
  └─────────┬─────────┘            └───────────────────┘
            ▼
  ┌───────────────────┐
  │ TRANSACTION       │
  │ IMPLEMENTATION    │ → Application Programs
  └───────────────────┘
```

## الفرق بين أنواع التصميم (Table للحفظ السريع)

| النوع | السؤال اللي بيجاوب عليه | الناتج | مستقل عن DBMS؟ |
|---|---|---|---|
| **Conceptual Design** | *إيه الكيانات والعلاقات؟* | Conceptual Schema (ERD) | ✅ نعم (DBMS-independent) |
| **Logical Design** | *إزاي أحوّلها لجداول ونموذج بيانات؟* | Relational Schema | نصف (نموذج بيانات محدد) |
| **Physical Design** | *إزاي تتخزن على القرص؟* | Internal Schema (Indexes, Files) | ❌ DBMS-specific |

> 🔑 **نقطة امتحانية:** خط الفاصل بين DBMS-independent و DBMS-specific بيمر بين Conceptual/Functional Design (فوق) وبين Logical Design (تحت).

---

# 🔷 المستوى 2: نموذج الكيان والعلاقة (The ER Model)

> الـ **ER Model** (Entity-Relationship Model) هو **نموذج بيانات مفاهيمي عالي المستوى** (high-level conceptual data model) — بيعبّر عن هيكل البيانات **بدون** التفكير في التخزين الفعلي.

## 1. الكيان (Entity) والنوع الكياني (Entity Type)

| المصطلح | التعريف | مثال |
|---|---|---|
| **Entity** | كائن محدد في الـ Miniworld | الموظف *John Smith*، القسم *Research* |
| **Entity Type** | تصنيف/مجموعة كيانات ليها نفس الخصائص | `EMPLOYEE`, `DEPARTMENT`, `PROJECT` |
| **Entity Set** | **المجموعة الفعلية الحالية** من كيانات النوع المخزنة في قاعدة البيانات | كل موظفي الشركة المخزنين دلوقتي |

> ⚠️ **سؤال شائع:** *Entity Type* هو **الوصف/السكيمة**، و*Entity Set* هو **الحالة الحالية** (current state of stored entities). الاسم نفسه ممكن يستخدم للاتنين.

## 2. الخصائص (Attributes) — أنواعها بالتفصيل

### أ. حسب البنية (Structure)

| النوع | التعريف | مثال | الرسم في ERD (Chen) |
|---|---|---|---|
| **Simple (Atomic)** | قيمة أحادية غير قابلة للتقسيم | `SSN`, `Salary` | بيضاوي عادي ◯ |
| **Composite** | صفة من **أجزاء** (ممكن الأجزاء نفسها composite — شجرة) | `Name(Fname, Minit, Lname)` — `Address(Street_address(Number, Street, Apartment), City, State)` | بيضاوي متفرع لأجزاء |
| **Multi-valued** | الكيان الواحد ليه **أكتر من قيمة** | `{Color}` لسيارة، `{PreviousDegrees}` لطالب | **بيضاوي مزدوج** ⬭⬭ |

### ب. حسب طريقة الحصول على القيمة (Stored vs Derived)

| النوع | التعريف | مثال | الرسم |
|---|---|---|---|
| **Stored** | قيمة تُخزَّن فعليًا | `Birth_date` | عادي |
| **Derived** | قيمة **تُشتق** من صفة(ات) تانية | `Age` مشتقة من `Birth_date`؛ `Number_of_employees` في DEPARTMENT بتتشتق بعدّ الموظفين المرتبطين | **بيضاوي متقطع** ⬌ |

> 🔑 **القاعدة الذهبية:** مش منطقي نخزّن `Age` و`Birth_date` مع بعض — لأن العمر **يتغير مع الوقت** وكده هتحصل تناقضات. بنخزّن المشتق منها ونحسب الباقي.

### ج. تركيب ممكن: Composite + Multivalued مع بعض

مثال من السلايدز: `{PreviousDegrees(College, Year, Degree, Field)}`
- Multivalued لأن الطالب ممكن يكون عنده شهادات كتير.
- Composite لأن كل شهادة نفسها من 4 أجزاء.

### د. Key Attributes (صفات المفتاح)

- **Key Attribute:** صفة **يجب** أن تكون قيمتها فريدة لكل كيان في النوع الكياني.
- ممكن يكون **Composite** (مفتاح مركّب): `VehicleTagNumber(Number, State)`.
- ممكن يكون **أكتر من Key** لنفس النوع: السيارة عندها VIN وRegistration — الاتنين Keys.
- **الرسم:** اسم الصفة **مخطوط تحته خط** 🔑.

> 💡 الجدول الحفظي:
> - خط تحت الاسم = Key Attribute
> - بيضاوي مزدوج = Multivalued
> - بيضاوي متقطع = Derived
> - بيضاوي متفرّع = Composite

## 3. الرموز الكاملة لترميز Chen (Figure 3.14 — مهم جدًا للامتحان)

| الرمز | المعنى |
|---|---|
| مستطيل ▭ | **Entity** |
| مستطيل مزدوج ▭▭ | **Weak Entity** |
| معيّن ◇ | **Relationship** |
| معيّن مزدوج ◇◇ | **Identifying Relationship** |
| بيضاوي متصل بخط | **Attribute** |
| بيضاوي **مخطّط تحته** | **Key Attribute** |
| بيضاوي مزدوج | **Multivalued Attribute** |
| بيضاوي متقطع | **Derived Attribute** |
| بيضاوي متفرّع لأجزاء | **Composite Attribute** |
| `E1 ───◇ R ◇───▭▭ E2` (خط مزدوج عند E2) | **Total Participation** لـ E2 في R |
| `E1 ─1─◇ R ◇─N─ E2` | **Cardinality Ratio 1:N** |
| `(min, max)` جنب الكيان | **Structural Constraint** |

## 4. الكيان الضعيف (Weak Entity)

> **Weak Entity = كيان ماعندوش Key Attribute خاص بيه.**

### شرطان لازم يتحققوا:
1. يشارك في **Identifying Relationship** مع **Owner/Identifying Entity Type**.
2. هويته الكاملة بتتحدد من:
   - **Partial Key** (المفتاح الجزئي — اسمه **Discriminator**) + المفتاح بتاع الكيان المالك.

### مثال COMPANY (حافظه):
- `DEPENDENT` كيان ضعيف — ماعندوش SSN.
- `Name` في DEPENDENT هو **Partial Key** (خط متقطع تحته).
- `EMPLOYEE` هو **Identifying Entity**.
- العلاقة `DEPENDENTS_OF` هي **Identifying Relationship** (معيّن مزدوج).
- التكملة المركّبة: هوية الـ Dependent = `Employee's SSN + Dependent's Name`.

### مقارنة سريعة:

| المفهوم | Strong Entity | Weak Entity |
|---|---|---|
| Key Attribute | ✅ عنده | ❌ ماعندوش (عنده Partial Key بس) |
| الاعتماد | مستقل | Existence-dependent على Owner |
| الرسم | مستطيل واحد ▭ | مستطيل مزدوج ▭▭ |
| العلاقة | عادية | Identifying (معيّن مزدوج) |
| الهوية | مفتاحه الخاص | Partial Key + مفتاح المالك |

---

# 🔗 المستوى 2 (تابع): العلاقات (Relationships)

## 1. المفاهيم الأساسية

| المصطلح | التعريف |
|---|---|
| **Relationship** | ربط بين **كيانين أو أكتر** مع معنى محدد: *John Smith يشتغل في ProductX* |
| **Relationship Type** | تصنيف/سكيمة للعلاقات المتشابهة: `WORKS_ON`, `MANAGES` |
| **Relationship Set** | **الحالة الحالية** من نسخ العلاقات المخزنة |
| **Degree** | عدد أنواع الكيانات المشاركة |

### Degree — درجات العلاقة:
| الدرجة | الاسم | مثال |
|---|---|---|
| 1 | **Unary / Recursive** | `SUPERVISION`: موظف يشرف على موظف تاني (نفس الكيان بدورين) |
| 2 | **Binary** | أغلب العلاقات: `WORKS_FOR`, `MANAGES`, `WORKS_ON` |
| 3 | **Ternary** | `SUPPLY(SUPPLIER, PART, PROJECT)` |
| n | **n-ary** | حالات نادرة |

> 🔑 **Recursive Relationship مهمة:** في `SUPERVISION` نفس نوع الكيان `EMPLOYEE` بيشارك **مرتين بدورين مختلفين** (Roles): **Supervisor** و**Supervisee**. في الـ ERD **لازم نكتب أسماء الأدوار** عشان نفرّق بينهم.

## 2. Relationship Attributes (صفات العلاقة)

- العلاقة نفسها ممكن يكون ليها صفات!
- مثال: `Hours` في `WORKS_ON` — عدد ساعات الموظف في المشروع **ساعاته هو في المشروع ده بالذات**، فمش تخص الموظف لوحده ولا المشروع لوحده.

> ⚠️ **قاعدة مهمة جدًا من السلايد:** صفات العلاقة بتستخدم أساسًا مع علاقات **M:N** (زي `Hours` مع `WORKS_ON`). أما في علاقة **1:N** فممكن **تنقل الصفة لجهة الـ N** بدل ما تفضل على العلاقة. (لأن كل سجل في جهة N بيرتبط بجهة واحدة بس، فالقيمة تخصّه.)

## 3. القيود على العلاقات (Constraints on Relationships) — قلب الشابتر 🔥

عندك **نوعين مستقلين** من القيود، ولازم تفرّق بينهم:

### أ. Cardinality Ratio (أقصى عدد — Maximum)

بتحدد **أقصى** عدد نسخ علاقة ممكن يرتبط بكيان.

| النوع | المعنى | مثال COMPANY |
|---|---|---|
| **1:1** | عنصر ↔ عنصر واحد كحد أقصى | `MANAGES`: موظف يدير قسم واحد كحد أقصى، وقسم ليه مدير واحد |
| **1:N / N:1** | واحد ↔ كتير | `WORKS_FOR`: قسم واحد فيه موظفين كتير (N)، وكل موظف لقسم واحد (1) |
| **M:N** | كتير ↔ كتير | `WORKS_ON`: موظف يشتغل مشاريع كتير، ومشروع فيه موظفين كتير |

> 📌 **بيتكتب إزاي في Chen؟** بتحط الرقم `1` أو `N` أو `M` **جنب الكيان** على الخط الواصل للعلاقة.

### ب. Participation Constraint (أقل عدد — Minimum)

بتحدد **هل المشاركة إجبارية ولا اختيارية؟**

| النوع | المعنى | الرسم في Chen | مثال |
|---|---|---|---|
| **Total Participation** | كل كيان **لازم** يشارك (mandatory / existence-dependent) | **خط مزدوج** ▬▬ | كل DEPENDENT لازم يكون تابع لموظف |
| **Partial Participation** | المشاركة اختيارية (صفر مسموح) | **خط واحد** ▬ | مش كل موظف يدير قسم |

> 🔑 **أشهر غلطة في الامتحان:** الخط الواحد والخطين **مش** بيعبّروا عن 1:N — ده بيعبّر عن **Participation**! والأرقام 1 وN هي اللي بتحدد الـ **Cardinality**.

### ج. الدمج: Structural Constraint بتنسيق (min, max) 🎯

دي الصيغة **الأدق** لأنها بتحدد **أقل وأكبر** عدد في نفس الوقت:

```
EMPLOYEE ──(0,1)──◇ MANAGES ◇──(1,1)── DEPARTMENT
```

| القيمة | المعنى | أمثلة من السلايد |
|---|---|---|
| **(0,1)** | اختياري، بحد أقصى واحد | مشاركة EMPLOYEE في MANAGES: ممكن ميديرش حاجة، أو يدير قسم واحد كحد أقصى |
| **(1,1)** | إجباري، بالضبط واحد | مشاركة DEPARTMENT في MANAGES: كل قسم لازم ليه مدير واحد بالضبط |
| **(0,N)** | اختياري، كتير | مشاركة DEPARTMENT في WORKS_FOR: قسم ممكن ميكونش فيه موظفين |
| **(1,N)** | إجباري، واحد على الأقل | مشاركة EMPLOYEE في DEPENDENTS_OF... (كل تابع لازم يتبع موظف) |

#### 📖 طريقة القراءة الصحيحة (من السلايد نفسها):
> **"Read the min, max numbers next to the entity type, looking away from the entity type."**
> يعني: الأرقام اللي جنب الكيان بتقول **هذا الكيان** بيحضر كام مرة في العلاقة — مش الطرف التاني.

#### القواعد الرياضية للصيغة:
- لازم `min ≤ max`
- `min ≥ 0`
- `max ≥ 1`
- الافتراضي لو مفيش قيد: `(0, N)` = لا قيد

### د. جدول التحويل بين الاتنين (احفظه — بييجي MCQ)

| Participation | Cardinality | (min, max) المكافئ |
|---|---|---|
| Partial | 1 كحد أقصى | **(0,1)** |
| Total | 1 كحد أقصى | **(1,1)** |
| Partial | N كحد أقصى | **(0,N)** |
| Total | N كحد أقصى | **(1,N)** |

---

# 🏢 التطبيق الكامل: COMPANY Database (مثال المحاضرة)

## 1. المتطلبات (Requirements) — زي نستخرج الكيانات

بالقراءة بعناية نطلع 4 Entity Types: `DEPARTMENT`, `PROJECT`, `EMPLOYEE`, `DEPENDENT`

> ⚠️ نقطة ذهبية: صفات زي `Manager` و`Department` و`Works_on` ظهرت في البداية كـ **صفات**، لكن بعد التحليل **اتحولّت لعلاقات**! (Manager → MANAGES، Department of employee → WORKS_FOR). دي مهارة: **لما تلاقي صفة فيها اسم كيان تاني، فكّر إنها علاقة.**

## 2. العلاقات الستة (كلها Binary)

| العلاقة | بين مين ومين | Cardinality | Participation |
|---|---|---|---|
| `WORKS_FOR` | EMPLOYEE ↔ DEPARTMENT | N:1 | EMPLOYEE: Total (1,1) — DEPARTMENT: Partial (0,N) |
| `MANAGES` | EMPLOYEE ↔ DEPARTMENT | 1:1 | EMPLOYEE: Partial (0,1) — DEPARTMENT: Total (1,1) |
| `CONTROLS` | DEPARTMENT ↔ PROJECT | 1:N | PROJECT: Total (1,1) — DEPARTMENT: Partial (0,N) |
| `WORKS_ON` | EMPLOYEE ↔ PROJECT | M:N | مع صفة `Hours` |
| `SUPERVISION` | EMPLOYEE ↔ EMPLOYEE | 1:N Recursive | أدوار Supervisor / Supervisee |
| `DEPENDENTS_OF` | EMPLOYEE ↔ DEPENDENT | 1:N | DEPENDENT: Total — وهي Identifying Relationship |

## 3. مشاهدات من الـ ER Diagram الشامل (Figure 3.2):

- `Start_date` صفة على علاقة `MANAGES` (تاريخ ما الموظف بقى مدير).
- `Number_of_employees` صفة **مشتقة** (متقطعة) على DEPARTMENT.
- `Locations` صفة **متعددة القيم** (مزدوجة) على DEPARTMENT.
- `DEPENDENT` مستطيل مزدوج + معيّن مزدوج = Weak Entity معرّفة.
- `Hours` صفة على علاقة M:N.

## 4. نفس الـ Schema بتنسيق (min, max) (Figure 3.15)

أمثلة القراءة:
- `EMPLOYEE (1,1) ─ WORKS_FOR ─ DEPARTMENT (0,N)` → الموظف لازم يشتغل في قسم واحد بالضبط، والقسم يمكن أن يضم صفر أو أي عدد موظفين.
- `EMPLOYEE (0,1) ─ MANAGES ─ DEPARTMENT (1,1)` → الموظف قد يدير قسمًا واحدًا كحد أقصى، والقسم لابد أن يكون له مدير واحد.

---

# 📐 المستوى 3: الترميزات البديلة (Alternative Notations)

## 1. UML Class Diagrams

| مفهوم ER | نظيره في UML |
|---|---|
| Entity Type | **Class** (مستطيل مستدير بثلاث أقسام: Name / Attributes / Operations) |
| Relationship | **Association** (خط بين الكلاسات + اسمها) |
| Multiplicity | `1..1`, `0..*`، `0..1` |

### Multiplicity Notation في OMT/UML:
- `1..1` = بالضبط واحد (خط فقط)
- `0..*` = صفر أو كتير (خط بنقطة معبّاة ●)
- `0..1` = صفر أو واحد (خط بدائرة ○)

> 🔑 فرق مهم: في UML الرقم بيتحط **عند الطرف البعيد** (الرقم عند DEPARTMENT في WORKS_FOR بيقول كام قسم للموظف) — العكس من منطق Chen تقريبًا. خلي بالك من الطريقة اللي الدكتور بيسأل بيها.

## 2. Ternary Relationships (علاقات من الدرجة الثالثة) ⚠️

**قاعدة حفظ:** n-ary relationship **مش** معادلة لـ n علاقات binary!
- 3 علاقات binary ممكن تحمل **معلومة مختلفة** تمامًا عن ternary واحدة.
- مثال: `SUPPLY(SUPPLIER, PART, PROJECT)` مع صفة `Quantity` — معناها: المورّد ده ودّد **الكمية دي من القطعة دي للمشروع ده**.
- لو قسمتها binary (`CAN_SUPPLY`, `USES`, `SUPPLIES`) هتضيع معلومة **التوليفة الثلاثية** (من ودّد إيه لمين بالكمية كام).
- **الاستثناء:** لو علاقة binary معيّنة ممكن **تُشتق دائمًا** من العلاقة العليا، تبقى **redundant** (زائدة) ومينفعش تتخزن — مثال `TAUGHT_DURING` المشتقة من `OFFERS`.

### رسم القيود على العلاقات العليا:
- `(min,max)` على الأضلاع **لا تكفي وحدها** — بنحتاج معاها `1, M, N`.
- الـ `1` بتقول: الكيان ده ممكن يشارك في **حالة علاقة واحدة كحد أقصى** لكل توليفة من باقي الكيانات.

---

# 🔑 المفاتيح (Keys) — المراجعة الشاملة

| المفتاح | التعريف | ملاحظات الامتحان |
|---|---|---|
| **Super Key** | أي مجموعة صفات تكفي لتحديد الكيان بشكل فريد | ممكن تكون فيها صفات زيادة |
| **Candidate Key** | أصغر Super Key (مفيش جزء منها يكفي) | ممكن يكون أكتر من واحد |
| **Primary Key (PK)** | Candidate Key **مختار** للتمثيل | مخطوط تحته، **لا يقبل NULL** |
| **Partial Key (Discriminator)** | صفة ضعيفة تُكمل هوية الـ Weak Entity مع مفتاح المالك | خط **متقطع** تحتها |
| **Foreign Key (FK)** | عمود بيشاور على PK في جدول آخر | بيتحقق الـ Referential Integrity |
| **Composite Key** | مفتاح من **أكتر من عمود** | زي `Registration(Number, State)` |

### القيود (Constraints) — متخلطش بينهم:

| القيد | بيمنع إيه |
|---|---|
| `NOT NULL` | غياب القيمة |
| `UNIQUE` | تكرار القيمة |
| `PRIMARY KEY` | الاتنين مع بعض: فريد + إلزامي |
| `FOREIGN KEY` | إشارة لسجل **غير موجود** في الجدول المشار إليه |
| `CHECK` | قاعدة عمليات (زي `quantity > 0`) |

> 🔥 **سؤال كلاسيكي:** لو حاولت تسجّل موعد لمريض رقمه 999 ومش موجود في PATIENT → الـ DBMS **يرفض العملية** بسبب الـ FK. اسمه: **Referential Integrity Constraint**.

---

# 🧩 العلاقات بعيون SQL (Mapping Preview)

| Cardinality | الحل في الـ Relational Schema |
|---|---|
| **1:1** | حط الـ PK بتاع طرف في الطرف التاني (غالبًا طرف المشاركة الإجبارية) كـ FK |
| **1:N** | الـ FK بيتحط في جهة **الـ N** |
| **M:N** | **جدول وسيط Junction/Associative Table**: PK بتاعه = مركّب من الـ FKs الاتنين + ممكن يضيف صفات العلاقة (زي `Hours`) |

### مثال محكي:

```
APPOINTMENT(appointment_id PK, patient_id FK→PATIENT, doctor_id FK→DOCTOR, time, status)
```

> ⚠️ خطأ شائع: حفظ `patient_name` و`doctor_name` **داخل** جدول الموعد — ده تكرار (redundancy) وهيدمّر الـ Consistency. كل معلومة في مكانها الصح.

---

# 🧪 تطبيع قاعدة البيانات (Normalization) — لازم تتقنه

| المستوى | الشرط | بيعالج إيه |
|---|---|---|
| **1NF** | كل خلية قيمة **أحادية** (مفيش قوائم جوّه خلية) | Multivalued attributes |
| **2NF** | 1NF + كل صفة غير مفتاحية تعتمد على **الـ PK المركّب كاملًا** مش على جزء منه | Partial Dependency |
| **3NF** | 2NF + مفيش صفة غير مفتاحية تعتمد على صفة غير مفتاحية تانية | Transitive Dependency |

**المعادلة الحفظية:** كل صفة غير مفتاحية لازم تعتمد على **المفتاح... كله... ولا غير المفتاح** (the key, the whole key, and nothing but the key).

---

# 🗃️ SQL المراجعة السريعة

## مجموعات الأوامر:

| المجموعة | الوظيفة | الأوامر |
|---|---|---|
| **DDL** | تعريف الهيكل | `CREATE, ALTER, DROP` |
| **DML** | التعامل مع البيانات | `INSERT, UPDATE, DELETE` |
| **DQL** | الاسترجاع | `SELECT` |
| **DCL** | الصلاحيات | `GRANT, REVOKE` |
| **TCL** | المعاملات | `COMMIT, ROLLBACK, SAVEPOINT` |

## نقاط لا تقبل الخطأ:
- **`WHERE` vs `HAVING`:** WHERE يفلتر **قبل** التجميع، HAVING **بعد** `GROUP BY`.
- **`NULL`:** ميقارنش بـ `=` — الصح: `IS NULL` / `IS NOT NULL`.
- **JOINs:**
  - `INNER JOIN` = المتطابق بس.
  - `LEFT JOIN` = كل يسار + المتطابق.
  - `FULL OUTER JOIN` = الاتنين كلهم + NULL للناقص.
- **نسيّت WHERE في UPDATE/DELETE؟** = الكارثة: كل السجلات اتعدّلت/اتمسحت. افحص الأول بـ SELECT.

## مثال تجميع كامل:

```sql
SELECT doctor_id, COUNT(*) AS appointment_count
FROM appointment
WHERE status = 'CONFIRMED'      -- فلترة قبل التجميع
GROUP BY doctor_id
HAVING COUNT(*) > 10;           -- فلترة بعد التجميع
```

---

# 🔄 المعاملات و ACID

| الخاصية | المعنى | الصورة العملية |
|---|---|---|
| **Atomicity** | الكل أو لا شيء | مفيش نصف عملية دفع |
| **Consistency** | القيود تفضل صحيحة | الفاتورة متتعارضش مع قواعدها |
| **Isolation** | المعاملات المتزامنة متتداخلش | موظفين مبيغيّروش نفس السجل بشكل فاسد |
| **Durability** | المعتمد يفضل محفوظ | بعد COMMIT البيانات متمسحش بقفل التطبيق |

```sql
SAVEPOINT before_update;
UPDATE appointment SET status='CANCELLED' WHERE appointment_id=3001;
ROLLBACK TO before_update;   -- التراجع عن اللي بعد الـ Savepoint
COMMIT;                      -- اعتماد اللي فضل
```

---

# ⚡ الفهارس والأداء (Indexes & Query Optimization)

- الفهرس **بيسرّع القراءة/البحث** على عمود متكرر الاستعلام عنه (`WHERE patient_id = ...`).
- **التكلفة:** مساحة إضافية + أبطأ `INSERT/UPDATE/DELETE` (الفهرس لازم يتجدد).
- **متعملوش عشوائيًا:** افهم الـ **Execution Plan** الأول.

```sql
CREATE INDEX idx_appointment_patient ON appointment(patient_id);
```

---

# 🧠 أسئلة تدريب سريعة (MCQ)

**1. خط مزدوج بين Entity وRelationship بيعبّر عن:**
- a) Cardinality N
- b) **Total Participation ✅**
- c) Weak Entity

**2. `EMPLOYEE (0,1) ── MANAGES ── DEPARTMENT (1,1)` معناها:**
- a) كل موظف لازم يدير قسم
- b) **الموظف قد لا يدير أي قسم، والقسم لابد له مدير ✅**
- c) العلاقة M:N

**3. `Hours` في `WORKS_ON` هي:**
- a) صفة Entity
- b) **Relationship Attribute (تخص توليفة موظف+مشروع) ✅**
- c) Partial Key

**4. الـ Dependent في COMPANY مثال على:**
- a) Strong Entity بمفتاحين
- b) **Weak Entity بهوية مركّبة (Employee SSN + Name) ✅**
- c) Multivalued Attribute

**5. Ternary relationship:**
- a) تساوي 3 binary relationships دائمًا
- b) **ممكن تحمل معلومة مختلفة عن 3 binary ✅**

**6. صفة `Age` المشتقة من `Birth_date`:**
- a) تُخزَّن مع تاريخ اليوم
- b) **ليست مخزنة — تُحسب عند الطلب ✅**

**7. مشاركة DEPARTMENT في WORKS_FOR:**
- a) (1,1)
- b) **(0,N) ✅**

**8. في 1:N relationship، صفات العلاقة:**
- a) لا يمكن نقلها أبدًا
- b) **يمكن نقلها لجهة N ✅**

---

# 🎯 خطة الإتقان النهائية (Checklist)

- [ ] أفرّق بين Data / Database / DBMS / Database System
- [ ] أشرح Database Design Process وأميّز Conceptual / Logical / Physical
- [ ] أرسم وأقرأ ERD بترميز Chen كامل (كل الرموز)
- [ ] أصنّف أي صفة: Simple / Composite / Multivalued / Derived / Key / Partial Key
- [ ] أكتشف الـ Weak Entity وأرسمه بـ Identifying Relationship
- [ ] أحدد Cardinality (1:1, 1:N, M:N) وأميّزها عن Participation
- [ ] أقرأ وأكتب الـ (min,max) notation صح
- [ ] أطبّق كل ده على مثال COMPANY من غير ما أبص
- [ ] أحوّل أي ERD لجداول (Mapping) مع الـ PKs والـ FKs
- [ ] أحل أسئلة Normalization وSQL وTransactions وIndexes
- [ ] أعرف الاختلافات مع UML والعلاقات Ternary

---

> 💬 **الخلاصة في جملة واحدة:**
> *افهم المشكلة → صمّم ERD بالقيود → حوّل لجداول مفاتيحها صح → نفّذ SQL نظيف → امنع التكرار بالتطبيع واحمِ البيانات بالمعاملات والقيود.*
