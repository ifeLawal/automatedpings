## Crontab

https://crontab.guru/#*_*_*_*_*

## Airflow

https://towardsdatascience.com/getting-started-with-apache-airflow-df1aa77d7b1b
https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html#adding-directories-to-pythonpath

## Swagger docs

https://swagger.io/blog/api-development/automatically-generating-swagger-specifications-wi/


## Collection of XPath Definitions

grab_parent = "/.."
following_sibling_any_type = "following-sibling::*"
any_tagname_id = "//*[@id='value']"
any_tagname_any_attribute_with_value = "//*[*='value']"
get_text = "//*[@id='value']/text()"
get_values_for_attribute = "//@attribute"
get_elements_one_and_two = "//tagname | //tagname "
get_child_elements_of_tag = "//tagname/*"
get_last_child_element_of_tag = "//tagname/tagname[last()]"
get_one_before_last_child_element_of_tag = "//tagname/tagname[last()-1]"
get_child_elements_greater_than_the_first_position = "//tagname/tagname[position()>1]"
get_child_elements = "//tagname/child::* | //tagname/child::node() | //tagname/child::text()"
get_flattened_child_elements_array = "//tagname/descendant::* | //tagname/descendant::node() | //tagname/descendant::text()"
