// State management
const state = {
    filter: "all",
    categories: ["Work", "Personal", "Shopping", "Health"],
    selectedCategory: "all",
    todos: [
      {
        id: 1,
        text: "Review project requirements",
        status: "pending",
        priority: "high",
        dueDate: "2024-02-10",
        category: "Work",
        description: "",
      },
      {
        id: 2,
        text: "Update documentation",
        status: "in-progress",
        priority: "medium",
        dueDate: "2024-02-15",
        category: "Work",
        description: "",
      },
      {
        id: 3,
        text: "Schedule team meeting",
        status: "completed",
        priority: "low",
        dueDate: "2024-02-08",
        category: "Work",
        description: "",
      },
      {
        id: 4,
        text: "Prepare presentation slides",
        status: "pending",
        priority: "high",
        dueDate: "2024-02-12",
        category: "Work",
        description: "",
      },
    ],
    newTodo: "",
    newPriority: "medium",
    newDueDate: "",
    newCategory: "Work",
    newDescription: "",
    nextId: 5,
    showCompleted: true,
  
    // Filter todos based on current filters
    filterTodos() {
      return this.todos
        .filter((todo) => {
          if (this.filter === "all") return true;
          if (this.filter === "active") return todo.status !== "completed";
          if (this.filter === "completed") return todo.status === "completed";
          return todo.status === this.filter;
        })
        .filter((todo) => {
          if (this.selectedCategory === "all") return true;
          return todo.category === this.selectedCategory;
        });
    },
  
    // Add a new todo
    addTodo() {
      if (this.newTodo.trim()) {
        this.todos.push({
          id: this.nextId++,
          text: this.newTodo.trim(),
          status: "pending",
          priority: this.newPriority,
          dueDate: this.newDueDate || new Date().toISOString().split("T")[0],
          category: this.newCategory,
        });
        this.newTodo = "";
        this.newPriority = "medium";
        this.newDueDate = "";
        updateUI();
      }
    },
  
    // Remove a todo
    removeTodo(id) {
      this.todos = this.todos.filter((todo) => todo.id !== id);
      updateUI();
    },
  
    // Update todo status
    updateStatus(id, newStatus) {
      const todo = this.todos.find((t) => t.id === id);
      if (todo) todo.status = newStatus;
      updateUI();
    },
  
    // Get color for priority
    getPriorityColor(priority) {
      return (
        {
          high: "#EF4444",
          medium: "#F59E0B",
          low: "#10B981",
        }[priority] || "#6B7280"
      );
    },
  
    // Get color for status
    getStatusColor(status) {
      return (
        {
          pending: "#F59E0B",
          "in-progress": "#3B82F6",
          completed: "#10B981",
        }[status] || "#6B7280"
      );
    },
  };
  
  // DOM Elements
  const elements = {
    categoryNav: document.querySelector(".category-nav"),
    categoryTemplate: document.getElementById("category-template"),
    currentDate: document.querySelector(".current-date"),
    activeCount: document.querySelector(".active-count"),
    completedCount: document.querySelector(".completed-count"),
    taskInput: document.querySelector(".task-input"),
    prioritySelect: document.querySelector(".priority-select"),
    dateInput: document.querySelector(".date-input"),
    addTaskButton: document.querySelector(".add-task-button"),
    statusFilter: document.querySelector(".status-filter"),
    categoryFilter: document.querySelector(".category-filter"),
    categoryOptionTemplate: document.getElementById("category-option-template"),
    taskList: document.querySelector(".task-list"),
    taskTemplate: document.getElementById("task-template"),
    searchInput: document.querySelector(".search-input"),
  };
  
  // Initialize the UI
  function initUI() {
    // Set current date
    elements.currentDate.textContent = new Date().toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  
    // Render categories in nav
    renderCategories();
  
    // Render category options in filter
    renderCategoryOptions();
  
    // Set initial values
    elements.prioritySelect.value = state.newPriority;
  
    // Add event listeners
    elements.taskInput.addEventListener("input", handleTaskInputChange);
    elements.taskInput.addEventListener("keyup", handleTaskInputKeyup);
    elements.prioritySelect.addEventListener("change", handlePriorityChange);
    elements.dateInput.addEventListener("change", handleDateChange);
    elements.addTaskButton.addEventListener("click", handleAddTask);
    elements.statusFilter.addEventListener("change", handleStatusFilterChange);
    elements.categoryFilter.addEventListener(
      "change",
      handleCategoryFilterChange,
    );
    elements.searchInput.addEventListener("input", handleSearchInput);
  
    // Initial render
    updateUI();
  }
  
  // Render category buttons
  function renderCategories() {
    // Clear existing categories
    const existingButtons = elements.categoryNav.querySelectorAll(
      ".category-button:not([id])",
    );
    existingButtons.forEach((button) => button.remove());
  
    // Add "All" category button
    const allButton = document.createElement("button");
    allButton.className = "category-button";
    allButton.classList.toggle("active", state.selectedCategory === "all");
    allButton.innerHTML = "<span>All</span><span>Tasks</span>";
    allButton.addEventListener("click", () => {
      state.selectedCategory = "all";
      updateUI();
    });
    elements.categoryNav.appendChild(allButton);
  
    // Add category buttons
    state.categories.forEach((category) => {
      const template = elements.categoryTemplate.content.cloneNode(true);
      const button = template.querySelector(".category-button");
      const categoryName = template.querySelector(".category-name");
  
      categoryName.textContent = category;
      button.classList.toggle("active", state.selectedCategory === category);
  
      button.addEventListener("click", () => {
        state.selectedCategory = category;
        updateUI();
      });
  
      elements.categoryNav.appendChild(template);
    });
  }
  
  // Render category options in filter
  function renderCategoryOptions() {
    // Clear existing options except the first one
    const options = elements.categoryFilter.querySelectorAll(
      "option:not(:first-child)",
    );
    options.forEach((option) => option.remove());
  
    // Add category options
    state.categories.forEach((category) => {
      const template = elements.categoryOptionTemplate.content.cloneNode(true);
      const option = template.querySelector("option");
  
      option.textContent = category;
      option.value = category;
  
      elements.categoryFilter.appendChild(template);
    });
  }
  
  // Render task list
  function renderTasks() {
    // Clear existing tasks
    const existingTasks = elements.taskList.querySelectorAll(".task-item");
    existingTasks.forEach((task) => task.remove());
  
    // Get filtered todos
    const filteredTodos = state.filterTodos();
  
    // Add tasks
    filteredTodos.forEach((todo) => {
      const template = elements.taskTemplate.content.cloneNode(true);
      const taskItem = template.querySelector(".task-item");
      const priorityIndicator = template.querySelector(".priority-indicator");
      const statusSelect = template.querySelector(".status-select");
      const taskText = template.querySelector(".task-text");
      const dueDateValue = template.querySelector(".due-date-value");
      const deleteButton = template.querySelector(".delete-task-button");
  
      // Set task data
      taskItem.dataset.id = todo.id;
      priorityIndicator.classList.add(`priority-${todo.priority}`);
      statusSelect.value = todo.status;
      statusSelect.classList.add(`status-${todo.status}`);
      taskText.textContent = todo.text;
      if (todo.status === "completed") {
        taskText.classList.add("completed-task");
      }
      dueDateValue.textContent = new Date(todo.dueDate).toLocaleDateString();
  
      // Add event listeners
      statusSelect.addEventListener("change", (e) => {
        state.updateStatus(todo.id, e.target.value);
      });
  
      deleteButton.addEventListener("click", () => {
        state.removeTodo(todo.id);
      });
  
      elements.taskList.appendChild(template);
    });
  }
  
  // Update UI based on current state
  function updateUI() {
    // Update category buttons
    const categoryButtons = document.querySelectorAll(".category-button");
    categoryButtons.forEach((button) => {
      const categoryText = button.querySelector("span:first-child").textContent;
      const isAll = categoryText === "All";
      const category = isAll ? "all" : categoryText;
      button.classList.toggle("active", state.selectedCategory === category);
    });
  
    // Update counts
    elements.activeCount.textContent = state.todos.filter(
      (t) => t.status !== "completed",
    ).length;
    elements.completedCount.textContent = state.todos.filter(
      (t) => t.status === "completed",
    ).length;
  
    // Update filters
    elements.statusFilter.value = state.filter;
    elements.categoryFilter.value = state.selectedCategory;
  
    // Update task input
    elements.taskInput.value = state.newTodo;
    elements.prioritySelect.value = state.newPriority;
    elements.dateInput.value = state.newDueDate;
  
    // Render tasks
    renderTasks();
  }
  
  // Event Handlers
  function handleTaskInputChange(e) {
    state.newTodo = e.target.value;
  }
  
  function handleTaskInputKeyup(e) {
    if (e.key === "Enter") {
      state.addTodo();
    }
  }
  
  function handlePriorityChange(e) {
    state.newPriority = e.target.value;
  }
  
  function handleDateChange(e) {
    state.newDueDate = e.target.value;
  }
  
  function handleAddTask() {
    state.addTodo();
  }
  
  function handleStatusFilterChange(e) {
    state.filter = e.target.value;
    updateUI();
  }
  
  function handleCategoryFilterChange(e) {
    state.selectedCategory = e.target.value;
    updateUI();
  }
  
  function handleSearchInput(e) {
    const searchTerm = e.target.value.toLowerCase();
  
    if (searchTerm) {
      const filteredTasks = document.querySelectorAll(".task-item");
      filteredTasks.forEach((task) => {
        const taskText = task
          .querySelector(".task-text")
          .textContent.toLowerCase();
        if (taskText.includes(searchTerm)) {
          task.style.display = "";
        } else {
          task.style.display = "none";
        }
      });
    } else {
      // If search is empty, show all tasks
      const filteredTasks = document.querySelectorAll(".task-item");
      filteredTasks.forEach((task) => {
        task.style.display = "";
      });
    }
  }
  
  // Initialize the application
  document.addEventListener("DOMContentLoaded", initUI);
  