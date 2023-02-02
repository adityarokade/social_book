console.log("js good");




function getemail(email) {
   console.log(email)
   

   $.ajax({
                      url: 'http://127.0.0.1:8000/existing_file_ajax/',
                  //   url: '{% url "existing_file_ajax" %}',
                    data: {
                        'email': email
                    },
                    dataType: 'json',
                    success: function (data) {
                       if (data) {
                           console.log("okk")
                          console.log(data)
                          bookList = JSON.parse(data)
                          bookList = bookList.map(e => {
                        const book = {
                            ...e.fields,
                            id: e.pk
                        }

                        return book

                    })

                           // showbooksdata(data)
                          
                          
                          renderbooksTable()
                          
                            
                           
                        }
                    }
                });

};

function showbooksdata(data) {
   var a = document.getElementById('booksdata')
   a.innerHTML="{% for da1 in data %} <tr> <th>{{da1.title_of_book}}</th> <th>{{da1.Author_of_book}}</th> <th>{{da1.Year}}</th> <th>{{da1.cost_of_book}}</th> </tr> {% endfor %}"
   
   console.log(a)
};







function renderbooksTable() {
        console.log("Rendring Table book", bookList)
         document.getElementById('bookTable').classList.toggle('bookstable')
        let tableBody = document.getElementById("bookTableBodyId")
        tableBody.remove()

        let newBody = document.createElement("tbody");
        newBody.id = "bookTableBodyId"
        document.getElementById("bookTable").append(newBody)



        bookList.forEach(
            function (book, index) {

                const row = newBody.insertRow()
            //     const count = document.createElement("TD")
            //   count.innerHTML = index + 1
              
                const title_of_book = document.createElement("TD")
              title_of_book.innerHTML = book.title_of_book
              
               const Author_of_book = document.createElement("TD")
              Author_of_book.innerHTML = book.Author_of_book
              
                const Year = document.createElement("TD")
              Year.innerHTML = book.Year

              const cost_of_book = document.createElement("TD")
              cost_of_book.innerHTML = book.cost_of_book

              const description= document.createElement("TD")
              description.innerHTML = book.description

              const file= document.createElement("TD")
              file.innerHTML = book.file

              
               //  const gender = document.createElement("TD")
               //  gender.innerHTML = (employee.gender == "M") ? "Male" : "Female"
               //  const office = document.createElement("TD")
               //  office.innerHTML = employee.office.name

               //  const activeCol = document.createElement("TD")
               //  const check = document.createElement('input')
               //  check.type = 'checkbox'
               //  if (employee.active) {
               //      check.checked = "checked"
               //  }
               //  activeCol.appendChild(check)

               //  check.onchange = function () {
               //      employee.active = check.checked
               //      console.log(employee)
               //      const body = {
               //          ...employee,
               //          office: employee.office.id,
               //          csrfmiddlewaretoken
               //      }
               //      const csrftoken = getCookie('csrftoken');
               //      console.log({ body })
               //      $.ajax({
               //          headers: {
               //              'X-CSRFToken': csrftoken
               //          },
               //          method: "PUT",
               //          url: "/employee",
               //          data: JSON.stringify(body)
               //      })
               //          .done(function (response) {
               //              console.log(response)

               //          })
               //          .fail(function (response) {
               //              console.log(response)
               //          })
               //  }


                
                row.appendChild(title_of_book)
              row.appendChild(Author_of_book)
              row.appendChild(Year)
                row.appendChild(cost_of_book)
                row.appendChild(description)
                row.appendChild(file)
               //  
               //  row.appendChild(Year)
                
            }
        )
    }









//   xhr.onload = function () {
//      if (this.status === 200) {
//         console.log("We are done fetching employees!");
//       //   console.log(data.Author_of_book);
//         console.log(this.responseText.Author_of_book)
//             // let obj = JSON.parse(this.responseText);
//             // console.log(obj);
//             // let list = document.getElementById('list');
//             // str = "";
//             // for (key in obj)
//             // {
//             //     str += `<li>${obj[key].employee_name} </li>`;
//             // }
//             // list.innerHTML = str;
//         }
//         else{
//             console.log("Some error occured")
//         }
//     }

//     // send the request
//     xhr.send();
    

   
   
// $("#id_username").change(function () {
//       var username = $(this).val();

//       $.ajax({
//         url: '/ajax/validate_username/',
//         data: {
//           'username': username
//         },
//         dataType: 'json',
//         success: function (data) {
//           if (data.is_taken) {
//             alert("A user with this username already exists.");
//           }
//         }
//       });

//     });
    

    


