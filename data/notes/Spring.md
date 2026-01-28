
<h1 style="color:#8f8;">Spring 🌱</h1>

---

## Dependency Injection 
- Field Injection
- Constructor Injection 
- Setter Injection 
## Stereotype Annotations
- **service**: business logics
- **repository**: model operations 
- **controller**: APIs control
- **Component**: create bean of any clas

##### Description:-
- used to define role of any class within the application.
- most of them just increase readability.
- most of them has `@component` as parent.
- even interchanging them will not cause any problem cause they just increase readability and has same parent `@component`.
# Scopes of Beans
- **singleton**: Only one instance of the bean is created per Spring IoC container. This is the default scope. All requests for that bean will return the same instance. 

- **prototype**: A new instance of the bean is created every time it is requested from the container.

- **application**: One instance of the bean is created for the entire web application. It is similar to a singleton but at the `ServletContext` level.

- **request**: A new instance of the bean is created for each HTTP request. This scope is only applicable in web-aware Spring applications. 

- **session**: A new instance of the bean is created for each HTTP session. This scope is also only applicable in web-aware Spring applications. 
#### singleton VS application :-
In a cluster (horizontal scaled system) each application (instance) will have its own `application scoped bean` but all instances will share same `singleton scoped bean`

#### request VS session :-
`request beans` are active for a single request and response pair until response is sent. While `session beans` are active for a whole session eg. Until cookie or session id is maintained .

