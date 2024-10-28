### At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### How to paginate a dataset with simple `page` and `page_size` parameters

Pagination is the process of dividing a dataset into smaller, manageable chunks (pages). Using `page` and `page_size` parameters, you can retrieve specific subsets of data.

- **`page_size`**: Defines the number of items per page.
- **`page`**: Indicates which page of data to retrieve.

For instance, to get the third page of a dataset with 10 items per page:
```python
page_size = 10
page = 3
start_index = (page - 1) * page_size
end_index = start_index + page_size
paged_data = dataset[start_index:end_index]
