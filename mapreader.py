
class MapReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = None
        self.entity_content = []
    
    #TODO
    #Not essential anyways
    def remove_comments(self):
        before = ''
        i = 0
        cleaned = self.content
        for char in self.content:
            if before + char == '//':
                print("Comment found")
            before = char
            i += 1
        
    
    """
    Remove double spaces, double newlines and so on to make parsing easier.
    """
    def normalize(self):
        self.content = self.content.replace("\t", " ")
        self.content = self.content.replace("  ", " ").replace("  ", " ")
        self.content = self.content.replace("\n\n", "\n").replace("\n\n", "\n")
    
    
    def get_value(self, key, content):
        pos = content.find("\"" + key + "\"")
        nlpos = content.find("\n", pos)
        line = content[pos:nlpos]
        value = line.replace("\"" + key + "\"", "").replace(" \"", "").replace("\"", "")
        if value == "":
            return None
        return value
    
    def get_brush(self, content):
        s_pos = content.find("{")
        e_pos = content.find("}")
        if s_pos and e_pos:
            return content[s_pos+1:e_pos]
        else:
            return None
    
    
    def parse_brush_line(self, brush_line):
        start_pos = 0
        
        abcoords = []
        
        brush_line = brush_line.replace("( ", "(").replace(" )", ")").replace("  ", "").replace("  ", "")
    
        for i in range(0,3):
            p_start = brush_line.find("(", start_pos)
            p_end = brush_line.find(")", start_pos)
            c_line = brush_line[p_start+1:p_end]
           
            if p_start == -1 or p_end == -1:
                return
            
            coords = c_line.split(" ")
            start_pos = p_end + 1
            print(coords)
            abcoords.append(coords)
        
        
        s_pos = brush_line.find(" ", start_pos+1)
        tex = brush_line[start_pos+1:s_pos]
        print(tex, start_pos, s_pos)
        

    def parse_brush(self, brush_content):
        lines = brush_content.split("\n")
        
        for line in lines:
            if line == "":
                continue
            brush_line = self.parse_brush_line(line)
        
        #print(lines)
    
    def parse_entity(self, content):
        val = self.get_value("classname", content)
        brush = self.get_brush(content)
        self.parse_brush(brush)
        
    def divide_entities(self):
        temp_content = self.content
        open_count = 0
        close_count = 0
        open_pos = None
        close_pos = None
        i = 0
        
        for char in self.content:
            
            if char == "{":
                if open_count == 0:
                    open_pos = i
                open_count += 1
            
            if char == "}":
                close_count += 1
            
            if open_count == close_count and open_count != 0:
                open_count = 0
                close_count = 0
                close_pos = i
                entity_content = self.content[open_pos+1:close_pos]
                self.entity_content.append(entity_content)
                
            i += 1
        
    def load_map(self):
        with open(self.file_name, "rt+") as file:
            self.content = file.read()
        
        
        
        
    
    

