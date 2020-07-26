function enableCategoryComplaintList(catageryName)
{
    resetComplainCategory();
    let container = document.getElementById(catageryName);
    container.classList.remove('hide');
    container.classList.add('show');
}
function resetComplainCategory(){
    let listContainer = document.getElementsByClassName('complaint-category-list');
    for(let i=0;i<listContainer.length;i++)
    {
        listContainer[i].classList.remove('show');
        listContainer[i].classList.add('hide');
    }
}