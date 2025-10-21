# Glossary of Terms (Iteration 6)

| Term                     | Definition                                                                                                                                                                                 |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Document`               | A class that represents any type of resource available on the GoTriple platform, including articles, conference papers, research data, project descriptions.                               |
| `Auhtor`                 | The individual inside the class Role primarily responsible for creating the content of the document.                                                                                       |
| `Profile`                | Subclass of Agent. It is the way that GoTriple handle the author.                                                                                                                          |
| `Online Account`         | The OnlineAccount class represents the provision of some form of online service, by some party (indicated indirectly via a accountServiceHomepage) to some Agent.                          |
| `is claimed`             | A data property for highlight if the profile is claimed or not by an account created by an user.                                                                                           |
| `account`                | The account property relates a Agent to an OnlineAccount for which they are the sole account holder. See OnlineAccount for usage details.                                                  |
| `Identifier`             | An identifier that uniquely identities an entity.                                                                                                                                          |
| `Identifier scheme`      | The identifier scheme used to identify an entity.                                                                                                                                          |
| `fullname`               | A data property for define the string with the complete name of an author.                                                                                                                 |
| `uses schema identifier` | An object property permitting specification of the identifier scheme used to provide the identifier for an entity.                                                                         |
| `is role held by`        | A property relating a role in time that an agent holds, or a contribution situation that an agent makes, to that agent.                                                                    |
| `Agent`                  | An abstract class defining any kind of agents, such as a person, a group, an organization or a software agent.                                                                             |
| `role in time`           | A particular situation that describe a role an agent may have, that can be restricted to a particular time interval.                                                                       |
| `with role`              | An object property connecting an agent's role in time to a definition of the type of role held by this agent, specified as an instance of the class pro:Role or of one of its sub-classes. |
| `role`                   | A role an agent may have. Individual members of this class or its sub-classes are used to specify particular roles.                                                                        |
| `also known as`          | An object property for connect a profile with another profile, when they are the same agent but with different fullname.                                                                   |
